import functools
import operator

__all__ = [
    'FunnelUnpacker',
    'RatioUnpacker',
    'SumUnpacker'
]


class SumUnpacker:
    def __init__(self, fact, period, dimensions):
        self.fact = fact
        self.period = period
        self.dimensions = dimensions

    def __call__(self, table):
        unpack = table.aggregate(
            by=[*self.dimensions, self.period],
            mean=table[self.fact].mean(),
            count=table[self.fact].count()
        )

        # Artificially add rows with 0s when there are no data points for a given group at a given
        # period. For instance, there might not be any dentist claims in 2022, but if there some in
        # 2021, then we want to have a 0 recorded so that we can measure the difference.
        cartesian_product = functools.reduce(lambda x, y: x.cross_join(y), [table[[d]].distinct() for d in [*self.dimensions, self.period]])
        unpack = cartesian_product.left_join(unpack, cartesian_product.columns)[unpack.columns]
        unpack = unpack.mutate(
            mean=unpack['mean'].fillna(0),
            count=unpack['count'].fillna(0)
        )

        unpack = (
            unpack
            .group_by(*self.dimensions)
            .order_by(self.period)
            .mutate(
                mean_lag=unpack['mean'].lag(1),
                count_lag=unpack['count'].lag(1)
            )
        )
        unpack = unpack.mutate(
            inner=unpack['count_lag'] * (unpack['mean'] - unpack['mean_lag']),
            mix=(unpack['count'] - unpack['count_lag']) * unpack['mean']
        )
        return (
            unpack
            .order_by([self.period, *self.dimensions])
            .select([self.period, *self.dimensions, 'inner', 'mix'])
            .dropna(how="any")
        )


class MeanUnpacker:
    def __init__(self, fact, period, dimensions):
        self.fact = fact
        self.period = period
        self.dimensions = dimensions

    def __call__(self, table):

        unpack = table.aggregate(
            by=[*self.dimensions, self.period],
            sum=table[self.fact].sum(),
            count=table[self.fact].count()
        )

        # Artificially add rows with 0s when there are no data points for a given group at a given
        # period. For instance, there might not be any dentist claims in 2022, but if there some in
        # 2021, then we want to have a 0 recorded so that we can measure the difference.
        cartesian_product = functools.reduce(lambda x, y: x.cross_join(y), [table[[d]].distinct() for d in [*self.dimensions, self.period]])
        unpack = cartesian_product.left_join(unpack, cartesian_product.columns)[unpack.columns]
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
        unpack = unpack.group_by(self.dimensions).order_by(self.period).mutate(
            ratio_lag=unpack['ratio'].lag(1),
            share_lag=unpack['share'].lag(1),
            global_ratio_lag=unpack['global_ratio'].lag(1)
        )
        unpack = unpack.mutate(
            inner=unpack['share'] * (unpack['ratio'] - unpack['ratio_lag']),
            mix=(unpack['share'] - unpack['share_lag']) * (unpack['ratio_lag'] - unpack['global_ratio'])
        )
        return (
            unpack
            .order_by([self.period, *self.dimensions])
            .select([self.period, *self.dimensions, 'inner', 'mix'])
            .dropna(how="any")
        )



class FunnelUnpacker:
    def __init__(self, fact, period, dimensions):
        self.fact = fact
        self.period = period
        self.dimensions = dimensions

    def __call__(self, table):

        traffic_table = ibis.memtable(traffic, name="traffic")

        # Sum events by period and dimensions
        unpack = (
            traffic_table.group_by([period, *dimensions])
            .aggregate(**{step: traffic_table[step].sum() for step in funnel})
        )
        ratios = {
            (f'{num}_over_{den}' if den else num): (num, den)
            for den, num in [(None, funnel[0]), *zip(funnel, funnel[1:])]
        }
        ratio_names = list(ratios)

        unpack = unpack.mutate(**{
            ratio_name: unpack[num] / unpack[den]
            for ratio_name, (num, den) in ratios.items()
            if den
        })

        unpack = unpack.group_by(dimensions).order_by(period).mutate(**{
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
            .order_by([period, *dimensions])
            .select([
                period,
                *dimensions,
                *[col for col in unpack.schema() if col.endswith('_contribution')]
            ])
            .dropna(how="any")
        )
