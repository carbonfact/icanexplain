import collections
import random
import names
import pandas as pd


def make_claims_df():

    random.seed(42)

    # Function to generate a random cost based on the claim type and year
    def generate_claim_cost(claim_type, year):
        if claim_type == 'Dentist':
            base_cost = 100
        elif claim_type == 'Psychiatrist':
            base_cost = 150

        # Adjust cost based on year
        if year == 2021:
            base_cost *= 1.2
        elif year == 2023:
            base_cost *= 1.5

        # Add some random variation
        cost = random.uniform(base_cost - 20, base_cost + 20)
        return round(cost, 2)

    # Generating sample data
    claim_types = ['Dentist', 'Psychiatrist']
    years = [2021, 2022, 2023, 2024]
    people = ['John', 'Jane', 'Michael', 'Emily', 'William']

    data = []
    for year in years:
        new_people = (
            [names.get_first_name() for _ in range(random.randint(1, 3))]
            if year > 2021
            else []
        )
        existing_people = [person for person in people if random.random() > 0.3]
        people_this_year = existing_people + new_people
        people.extend(new_people)

        for person in people_this_year:
            num_claims = random.randint(1, 5)  # Random number of claims per existing customer per year
            for _ in range(num_claims):
                claim_type = random.choice(claim_types)
                cost = generate_claim_cost(claim_type, year)
                date = pd.to_datetime(f"{random.randint(1, 12)}/{random.randint(1, 28)}/{year}", format='%m/%d/%Y')
                data.append([person, claim_type, date, year, cost])

    # Create the DataFrame
    columns = ['person', 'claim_type', 'date', 'year', 'amount']
    claims_df = pd.DataFrame(data, columns=columns)

    # Indicate whether people are existing, new, or returning
    years_seen = collections.defaultdict(set)
    statuses = []
    for claim in claims_df.to_dict(orient='records'):
        years_seen[claim['person']].add(claim['year'])
        if claim['year'] - 1 in years_seen[claim['person']]:
            statuses.append('EXISTING')
        elif any(year < claim['year'] for year in years_seen[claim['person']]):
            statuses.append('RETURNING')
        elif not {year for year in years_seen[claim['person']] if year != claim['year']}:
            statuses.append('NEW')

    claims_df['status'] = statuses

    return claims_df


def test_claims():
    """

    >>> import ibis
    >>> import munpack

    >>> claims_df = make_claims_df()
    >>> claims_df.head()
      person    claim_type       date  year  amount status
    0   John       Dentist 2021-01-01  2021  123.62    NEW
    1   John       Dentist 2021-09-20  2021  108.75    NEW
    2   John       Dentist 2021-12-21  2021  122.45    NEW
    3   John  Psychiatrist 2021-10-09  2021  168.82    NEW
    4   John       Dentist 2021-03-23  2021  130.35    NEW

    The goal is to explain how the mean evolved over time. Let's take a look at it.

    >>> (
    ...     claims_df
    ...     .groupby('year')
    ...     .agg({'amount': 'mean'})
    ...     .assign(diff=lambda x: x.amount.diff())
    ...     .reset_index()
    ... )
       year      amount       diff
    0  2021  145.808889        NaN
    1  2022  112.676667 -33.132222
    2  2023  173.043667  60.367000
    3  2024  122.920625 -50.123042

    Here's the breakdown by claim type:

    >>> (
    ...     claims_df
    ...     .groupby(['year', 'claim_type'])
    ...     ['amount'].agg(['mean', 'count'])
    ...     .reset_index()
    ... )
       year    claim_type       mean  count
    0  2021       Dentist  122.87200      5
    1  2021  Psychiatrist  174.48000      4
    2  2022       Dentist   98.37500      4
    3  2022  Psychiatrist  141.28000      2
    4  2023       Dentist  148.36500     20
    5  2023  Psychiatrist  222.40100     10
    6  2024       Dentist   97.68250      8
    7  2024  Psychiatrist  148.15875      8

    The theory is that however we unpack the metric, the figures we find should add up to the same
    yearly total.

    >>> unpacker = munpack.MeanUnpacker(
    ...     fact='amount',
    ...     period='year',
    ...     dimensions=['claim_type']
    ... )
    >>> unpack = unpacker(ibis.memtable(claims_df))
    >>> unpack.execute()
       year    claim_type      inner        mix
    0  2022       Dentist -16.331333   1.132815
    1  2022  Psychiatrist -11.066667  -6.867037
    2  2023       Dentist  33.326667  -0.000000
    3  2023  Psychiatrist  27.040333  -0.000000
    4  2024       Dentist -25.341250  -4.240729
    5  2024  Psychiatrist -37.121125  16.580063

    Let's check that the sum of the inner and mix columns add up as expected.

    >>> (
    ...     unpack
    ...     .execute()
    ...     .groupby('year')
    ...     .apply(lambda x: (x.inner + x.mix).sum())
    ...     .rename('diff')
    ...     .reset_index()
    ... )
       year       diff
    0  2022 -33.132222
    1  2023  60.367000
    2  2024 -50.123042

    """


def test_claims_with_gaps():
    """

    >>> import ibis
    >>> import munpack

    >>> claims_df = make_claims_df()
    >>> claims_df = claims_df.drop(index=claims_df.query('year == 2021 and claim_type == "Dentist"').index)
    >>> claims_df = claims_df.drop(index=claims_df.query('year == 2022 and claim_type == "Psychiatrist"').index)
    >>> claims_df = claims_df.drop(index=claims_df.query('year == 2023 and claim_type == "Psychiatrist"').index)

    >>> (
    ...     claims_df
    ...     .groupby('year')
    ...     .agg({'amount': 'mean'})
    ...     .assign(diff=lambda x: x.amount.diff())
    ...     .reset_index()
    ... )
       year      amount       diff
    0  2021  174.480000        NaN
    1  2022   98.375000 -76.105000
    2  2023  148.365000  49.990000
    3  2024  122.920625 -25.444375

    >>> unpacker = munpack.MeanUnpacker(
    ...     fact='amount',
    ...     period='year',
    ...     dimensions=['claim_type']
    ... )
    >>> unpack = unpacker(ibis.memtable(claims_df))
    >>> unpack.execute()
       year    claim_type      inner        mix
    0  2022       Dentist  98.375000 -98.375000
    1  2022  Psychiatrist  -0.000000 -76.105000
    2  2023       Dentist  49.990000  -0.000000
    3  2023  Psychiatrist   0.000000  -0.000000
    4  2024       Dentist -25.341250 -12.722187
    5  2024  Psychiatrist  74.079375 -61.460313

    """
