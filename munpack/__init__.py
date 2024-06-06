import functools
import operator

from . import datasets

__all__ = [
    'FunnelUnpacker',
    'MeanUnpacker',
    'SumUnpacker',
    'datasets'
]


def cartesian_product(table, columns):
    return functools.reduce(lambda x, y: x.cross_join(y), [table[[d]].distinct() for d in columns])


class SumUnpacker:
    def __init__(self, fact, period: str | list[int], group: str | list[int]):
        self.fact = fact
        self.period = [period] if isinstance(period, str) else period
        self.group = [group] if isinstance(group, str) else group

    def __call__(self, table):
        unpack = table.aggregate(
            by=[*self.group, *self.period],
            mean=table[self.fact].mean(),
            count=table[self.fact].count()
        )

        # Artificially add rows with 0s when there are no data points for a given group at a given
        # period. For instance, there might not be any dentist claims in 2022, but if there some in
        # 2021, then we want to have a 0 recorded so that we can measure the difference.
        cart = cartesian_product(table, [*self.group, *self.period])
        unpack = cart.left_join(unpack, cart.columns)[unpack.columns]
        unpack = unpack.mutate(
            mean=unpack['mean'].fillna(0),
            count=unpack['count'].fillna(0)
        )

        # Calculate lag values
        unpack = (
            unpack
            .group_by([*self.group, *self.period[1:]])
            .order_by(self.period)
            .mutate(
                mean_lag=unpack['mean'].lag(1),
                count_lag=unpack['count'].lag(1)
            )
        )

        # Calculate the inner and mix effects
        unpack = unpack.mutate(
            inner=unpack['count_lag'] * (unpack['mean'] - unpack['mean_lag']),
            mix=(unpack['count'] - unpack['count_lag']) * unpack['mean']
        )

        return (
            unpack
            .order_by([*self.period, *self.group])
            .select([*self.period, *self.group, 'inner', 'mix'])
            .dropna(how="any")
        )


class MeanUnpacker:
    def __init__(self, fact, period: str | list[int], group: str | list[int]):
        self.fact = fact
        self.period = [period] if isinstance(period, str) else period
        self.group = [group] if isinstance(group, str) else group

    def __call__(self, table):

        unpack = table.aggregate(
            by=[*self.group, *self.period],
            sum=table[self.fact].sum(),
            count=table[self.fact].count()
        )

        # Artificially add rows with 0s when there are no data points for a given group at a given
        # period. For instance, there might not be any dentist claims in 2022, but if there some in
        # 2021, then we want to have a 0 recorded so that we can measure the difference.
        cart = cartesian_product(table, [*self.group, *self.period])
        unpack = cart.left_join(unpack, cart.columns)[unpack.columns]
        unpack = unpack.mutate(
            sum=unpack['sum'].fillna(0),
            count=unpack['count'].fillna(0)
        )
        unpack = unpack.mutate(ratio=(unpack['sum'] / unpack['count']).fillna(0))

        yearly_figures = unpack.group_by(self.period).aggregate(
            sum_sum=unpack['sum'].sum(),
            count_sum=unpack['count'].sum()
        )
        unpack = unpack.left_join(yearly_figures, self.period)
        unpack = unpack.mutate(
            share=unpack['count'] / unpack['count_sum'],
            global_ratio=unpack['sum_sum'] / unpack['count_sum']
        )

        # Calculate lag values
        # 🐲 It's a bit tricky, but in cases where more than one period column is provided, they
        # it affects the lag calculation. For instance, if we have year and month, then we want to
        # calculate the lag for the same month in the previous year. This only applies to the case
        # where the period is a list of columns.
        unpack = unpack.group_by([*self.group, *self.period[1:]]).order_by(self.period).mutate(
            ratio_lag=unpack['ratio'].lag(1),
            share_lag=unpack['share'].lag(1),
            global_ratio_lag=unpack['global_ratio'].lag(1)
        )

        # Calculate the inner and mix effects
        unpack = unpack.mutate(
            inner=unpack['share'] * (unpack['ratio'] - unpack['ratio_lag']),
            mix=(unpack['share'] - unpack['share_lag']) * (unpack['ratio_lag'] - unpack['global_ratio'])
        )

        return (
            unpack
            .order_by([*self.period, *self.group])
            .select([*self.period, *self.group, 'inner', 'mix'])
            .dropna(how="any")
        )



class FunnelUnpacker:
    def __init__(self, funnel: list[str], period: str | list[int], group: str | list[int]):
        self.funnel = funnel
        self.period = [period] if isinstance(period, str) else period
        self.group = [group] if isinstance(group, str) else group

    def __call__(self, table):

        # Sum events by period and dimensions
        unpack = (
            table.group_by([*self.period, *self.group])
            .aggregate(**{step: table[step].sum() for step in self.funnel})
        )
        ratios = {
            (f'{num}_over_{den}' if den else num): (num, den)
            for den, num in [(None, self.funnel[0]), *zip(self.funnel, self.funnel[1:])]
        }
        ratio_names = list(ratios)

        unpack = unpack.mutate(**{
            ratio_name: unpack[num] / unpack[den]
            for ratio_name, (num, den) in ratios.items()
            if den
        })

        unpack = unpack.group_by([*self.group, *self.period[1:]]).order_by(self.period).mutate(**{
            f'{ratio_name}_lag': unpack[ratio_name].lag(1)
            for ratio_name in ratios
        })

        unpack = unpack.mutate(**{
            f'{ratio_name}_contribution': functools.reduce(
                operator.mul,
                [
                    *[unpack[ratio_name] for ratio_name in ratio_names[:i]],
                    unpack[ratio_names[i]] - unpack[f"{ratio_names[i]}_lag"],
                    *[unpack[f'{ratio_name}_lag'] for ratio_name in ratio_names[i+1:]]
                ]
            )
            for i, ratio_name in enumerate(ratio_names)
        })

        return (
            unpack
            .order_by([*self.period, *self.group])
            .select([
                *self.period,
                *self.group,
                *[col for col in unpack.schema() if col.endswith('_contribution')]
            ])
            .dropna(how="any")
        )
