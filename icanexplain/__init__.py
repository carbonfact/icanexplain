import abc
import functools
import operator

import ibis  # type: ignore[import]

from . import datasets

__all__ = ["FunnelExplainer", "MeanExplainer", "SumExplainer", "datasets"]


def cartesian_product(table, columns):
    return functools.reduce(
        lambda x, y: x.cross_join(y), [table[[d]].distinct() for d in columns]
    )


def is_pandas_dataframe(obj):
    try:
        import pandas as pd

        return isinstance(obj, pd.DataFrame)
    except ImportError:
        # pandas is not installed
        return False


def is_polars_dataframe(obj):
    try:
        import polars as pl  # type: ignore[import]

        return isinstance(obj, pl.DataFrame)
    except ImportError:
        # polars is not installed
        return False


def coerce_table(method):
    @functools.wraps(method)
    def _impl(self, table):
        if is_pandas_dataframe(table):
            return method(self, ibis.memtable(table[self._necessary_columns]))
        if is_polars_dataframe(table):
            return method(self, ibis.memtable(table[self._necessary_columns]))
        return method(self, table)

    return _impl


class Unpacker(abc.ABC):
    def __init__(
        self,
        fact: str,
        period: str | list[str],
        group: str | list[str] | None = None,
        count: str | None = None,
    ):
        self.fact = fact
        self.period = [period] if isinstance(period, str) else period
        self.group = [group] if isinstance(group, str) else (group if group else [])
        self.count = count

    @abc.abstractproperty
    def _necessary_columns(self):
        pass

    @abc.abstractmethod
    def _explanation(self, table: ibis.Table):
        pass

    @abc.abstractmethod
    def _format(self, explanation: ibis.Table):
        pass

    def __call__(self, table):
        explanation = self._explanation(table)
        explanation_fmt = self._format(explanation)
        if is_pandas_dataframe(table):
            return explanation_fmt.execute().set_index([*self.period, *self.group])
        if is_polars_dataframe(table):
            return explanation_fmt.execute()
        return explanation_fmt

    def plot(self, table):
        import altair as alt  # type: ignore[import]
        import pandas as pd

        explanation = self._explanation(table)
        if not isinstance(explanation, pd.DataFrame):
            explanation = explanation.execute()

        charts = []
        total = pd.DataFrame({"label": [], "total": []})

        for i, (period, period_explanation) in enumerate(
            explanation.sort_values(self.period).groupby(self.period)
        ):
            if i > 0:
                contributions = pd.concat(
                    [
                        (
                            period_explanation[[*self.period, *self.group, "inner"]]
                            .rename(columns={"inner": "impact"})
                            .assign(kind="inner")
                        ),
                        (
                            period_explanation[[*self.period, *self.group, "mix"]]
                            .rename(columns={"mix": "impact"})
                            .assign(kind="mix")
                        ),
                    ]
                )
                prev_total_value = total["total"].iloc[-1]
                contributions = contributions.sort_values("impact", ascending=False)
                contributions["end"] = (
                    prev_total_value + contributions["impact"].cumsum()
                )
                contributions["start"] = (
                    contributions["end"].shift(1).fillna(prev_total_value)
                )
                label_cols = [*self.period, *self.group, "kind"]
                contributions["label"] = contributions[label_cols].agg(
                    lambda x: " • ".join(x.astype(str)), axis="columns"
                )
                contributions["is_positive"] = contributions["impact"] > 0

                chart = (
                    alt.Chart(contributions)
                    .mark_bar()
                    .encode(
                        y=alt.Y("label:O", sort=None, axis=alt.Axis(title=None)),
                        x=alt.X("start:Q", axis=alt.Axis(title=self.fact)),
                        x2="end:Q",
                        color=alt.Color(
                            "is_positive:N",
                            scale=alt.Scale(
                                domain=[True, False], range=["green", "red"]
                            ),
                            legend=None,
                        ),
                        tooltip=[*label_cols, "impact"],
                    )
                )
                charts.append(chart)

            total = pd.DataFrame(
                {
                    "label": [period],
                    "total": (
                        [
                            (
                                period_explanation["count"]
                                * period_explanation["ratio"]
                            ).sum()
                            / period_explanation["count"].sum()
                        ]
                        if isinstance(self, MeanExplainer)
                        else [(period_explanation["total"]).sum()]
                    ),
                }
            )

            chart = (
                alt.Chart(total)
                .mark_bar()
                .encode(x="total:Q", y=alt.X("label:O", sort=None), tooltip=["total"])
            )
            charts.append(chart)

        return alt.layer(*charts).interactive()


class SumExplainer(Unpacker):
    @property
    def _necessary_columns(self):
        return [
            self.fact,
            *self.period,
            *self.group,
            *([self.count] if self.count else []),
        ]

    @coerce_table
    def _explanation(self, table):
        explanation = table.aggregate(
            by=[*self.group, *self.period],
            mean=(
                (table[self.fact] * table[self.count]).sum() / table[self.count].sum()
                if self.count
                else table[self.fact].mean()
            ),
            count=(table[self.count].sum() if self.count else table[self.fact].count()),
        )

        # Artificially add rows with 0s when there are no data points for a given group at a given
        # period. For instance, there might not be any dentist claims in 2022, but if there some in
        # 2021, then we want to have a 0 recorded so that we can measure the difference.
        cart = cartesian_product(table, [*self.group, *self.period])
        explanation = cart.left_join(explanation, cart.columns)[explanation.columns]
        explanation = explanation.mutate(
            mean=explanation["mean"].fillna(0), count=explanation["count"].fillna(0)
        )

        # Calculate lag values
        # Usually one or more group keys are provided. But if they aren't, there is no need to
        # aggregate the data by the group keys. In this case, we can just calculate the lag values
        # along the period column.
        # TODO: it would be nice to have a more elegant way to handle this.
        if lag_key := [*self.group, *self.period[1:]]:
            explanation = (
                explanation.group_by(lag_key)
                .order_by(self.period)
                .mutate(
                    mean_lag=explanation["mean"].lag(1),
                    count_lag=explanation["count"].lag(1),
                )
            )
        else:
            explanation = explanation.order_by(self.period).mutate(
                mean_lag=explanation["mean"].lag(1),
                count_lag=explanation["count"].lag(1),
            )

        # Calculate the inner and mix effects
        return explanation.mutate(
            total=explanation["count"] * explanation["mean"],
            inner=explanation["count_lag"]
            * (explanation["mean"] - explanation["mean_lag"]),
            mix=(explanation["count"] - explanation["count_lag"]) * explanation["mean"],
        )

    def _format(self, explanation):
        return (
            explanation.order_by([*self.period, *self.group])
            .select([*self.period, *self.group, "inner", "mix"])
            .dropna(how="any")
        )


class MeanExplainer(Unpacker):
    @property
    def _necessary_columns(self):
        return [
            self.fact,
            *self.period,
            *self.group,
            *([self.count] if self.count else []),
        ]

    @coerce_table
    def _explanation(self, table):
        explanation = table.aggregate(
            by=[*self.group, *self.period],
            sum=(
                (table[self.fact] * table[self.count]).sum()
                if self.count
                else table[self.fact].sum()
            ),
            count=(table[self.count].sum() if self.count else table[self.fact].count()),
        )

        # Artificially add rows with 0s when there are no data points for a given group at a given
        # period. For instance, there might not be any dentist claims in 2022, but if there some in
        # 2021, then we want to have a 0 recorded so that we can measure the difference.
        cart = cartesian_product(table, [*self.group, *self.period])
        explanation = cart.left_join(explanation, cart.columns)[explanation.columns]
        explanation = explanation.mutate(
            sum=explanation["sum"].fillna(0), count=explanation["count"].fillna(0)
        )
        explanation = explanation.mutate(
            ratio=(explanation["sum"] / explanation["count"]).fillna(0)
        )

        yearly_figures = explanation.group_by(self.period).aggregate(
            sum_sum=explanation["sum"].sum(), count_sum=explanation["count"].sum()
        )
        explanation = explanation.left_join(yearly_figures, self.period)
        explanation = explanation.mutate(
            share=explanation["count"] / explanation["count_sum"],
            global_ratio=explanation["sum_sum"] / explanation["count_sum"],
        )

        # Calculate lag values
        # 🐲 It's a bit tricky, but in cases where more than one period column is provided, they
        # it affects the lag calculation. For instance, if we have year and month, then we want to
        # calculate the lag for the same month in the previous year. This only applies to the case
        # where the period is a list of columns.
        if by := [*self.group, *self.period[1:]]:
            explanation = (
                explanation.group_by(by)
                .order_by(self.period)
                .mutate(
                    ratio_lag=explanation["ratio"].lag(1),
                    share_lag=explanation["share"].lag(1),
                    global_ratio_lag=explanation["global_ratio"].lag(1),
                )
            )
        else:
            explanation = explanation.order_by(self.period).mutate(
                ratio_lag=explanation["ratio"].lag(1),
                share_lag=explanation["share"].lag(1),
                global_ratio_lag=explanation["global_ratio"].lag(1),
            )

        # Calculate the inner and mix effects
        return explanation.mutate(
            inner=explanation["share"]
            * (explanation["ratio"] - explanation["ratio_lag"]),
            mix=(explanation["share"] - explanation["share_lag"])
            * (explanation["ratio_lag"] - explanation["global_ratio"]),
        )

    def _format(self, explanation):
        return (
            explanation.order_by([*self.period, *self.group])
            .select([*self.period, *self.group, "inner", "mix"])
            .dropna(how="any")
        )


class FunnelExplainer(Unpacker):
    def __init__(
        self, funnel: list[str], period: str | list[str], group: str | list[str]
    ):
        self.funnel = funnel
        self.period = [period] if isinstance(period, str) else period
        self.group = [group] if isinstance(group, str) else group

    @property
    def _necessary_columns(self):
        return [*self.funnel, *self.period, *self.group]

    @coerce_table
    def _explanation(self, table):
        # Sum events by period and dimensions
        explanation = table.group_by([*self.period, *self.group]).aggregate(
            **{step: table[step].sum() for step in self.funnel}
        )
        ratios = {
            (f"{num}_over_{den}" if den else num): (num, den)
            for den, num in [(None, self.funnel[0]), *zip(self.funnel, self.funnel[1:])]
        }
        ratio_names = list(ratios)

        explanation = explanation.mutate(
            **{
                ratio_name: explanation[num] / explanation[den]
                for ratio_name, (num, den) in ratios.items()
                if den
            }
        )

        explanation = (
            explanation.group_by([*self.group, *self.period[1:]])
            .order_by(self.period)
            .mutate(
                **{
                    f"{ratio_name}_lag": explanation[ratio_name].lag(1)
                    for ratio_name in ratios
                }
            )
        )

        explanation = explanation.mutate(
            **{
                f"{ratio_name}_contribution": functools.reduce(
                    operator.mul,
                    [
                        *[explanation[ratio_name] for ratio_name in ratio_names[:i]],
                        explanation[ratio_names[i]]
                        - explanation[f"{ratio_names[i]}_lag"],
                        *[
                            explanation[f"{ratio_name}_lag"]
                            for ratio_name in ratio_names[i + 1 :]
                        ],
                    ],
                )
                for i, ratio_name in enumerate(ratio_names)
            }
        )

        return explanation

    def _format(self, explanation):
        return (
            explanation.order_by([*self.period, *self.group])
            .select(
                [
                    *self.period,
                    *self.group,
                    *[
                        col
                        for col in explanation.schema()
                        if col.endswith("_contribution")
                    ],
                ]
            )
            .dropna(how="any")
        )
