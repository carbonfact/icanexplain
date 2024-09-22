import random
import pandas as pd


def make_claims() -> pd.DataFrame:
    random.seed(42)

    # Function to generate a random cost based on the claim type and year
    def generate_claim_cost(claim_type, year):
        if claim_type == "Dentist":
            base_cost = 100
        elif claim_type == "Psychiatrist":
            base_cost = 150
        elif claim_type == "General Physician":
            base_cost = 80
        elif claim_type == "Physiotherapy":
            base_cost = 120
        else:
            base_cost = 50

        # Adjust cost based on year
        if year == 2021:
            base_cost *= 1.2
        elif year == 2023:
            base_cost *= 1.5

        # Add some random variation
        cost = random.uniform(base_cost - 20, base_cost + 20)
        return round(cost, 2)

    # Generating sample data
    claim_types = ["Dentist", "Psychiatrist", "General Physician", "Physiotherapy"]
    years = [2021, 2022, 2023]
    people = [
        "John",
        "Jane",
        "Michael",
        "Emily",
        "William",
        "Emma",
        "Daniel",
        "Olivia",
        "Lucas",
        "Ava",
    ]

    data = []
    for year in years:
        for person in people:
            num_claims = random.randint(
                1, 5
            )  # Random number of claims per person per year
            for _ in range(num_claims):
                claim_type = random.choice(claim_types)
                cost = generate_claim_cost(claim_type, year)
                date = pd.to_datetime(
                    f"{random.randint(1, 12)}/{random.randint(1, 28)}/{year}",
                    format="%m/%d/%Y",
                )
                data.append([person, claim_type, date, year, cost])

    # Create the DataFrame
    columns = ["person", "claim_type", "date", "year", "amount"]
    claims = pd.DataFrame(data, columns=columns)

    return claims


def test_claims():
    """

    >>> import icanexplain as ice

    >>> claims = make_claims()
    >>> claims.head()
        person     claim_type       date  year  amount
    0     John        Dentist 2021-04-08  2021  129.66
    1     Jane        Dentist 2021-09-03  2021  127.07
    2     Jane  Physiotherapy 2021-02-07  2021  125.27
    3  Michael        Dentist 2021-12-21  2021  122.45
    4  Michael  Physiotherapy 2021-10-09  2021  132.82

    The goal is to explain the evolution of total claims amount over time. Let's take a look at the
    yearly evolution.

    >>> (
    ...     claims
    ...     .groupby('year')
    ...     .agg({'amount': 'sum'})
    ...     .assign(diff=lambda x: x.amount.diff())
    ...     .reset_index()
    ... )
       year   amount     diff
    0  2021  3814.54      NaN
    1  2022  2890.29  -924.25
    2  2023  4178.03  1287.74

    The theory is that the figures we find should add up to the same yearly total, however we
    explanation the metric.

    >>> explainer = ice.SumExplainer(
    ...     fact='amount',
    ...     period='year',
    ...     group='claim_type'
    ... )
    >>> explanation = explainer(claims)
    >>> explanation
                                 inner         mix
    year claim_type
    2022 Dentist           -170.700000 -311.240000
         General Physician  -95.053333  249.693333
         Physiotherapy     -122.880000 -339.450000
         Psychiatrist      -282.030000  147.410000
    2023 Dentist            338.180000  480.330000
         General Physician  313.151429 -236.051429
         Physiotherapy      185.125000  524.575000
         Psychiatrist       544.140000 -861.710000

    Let's check that the sum of the inner and mix columns add up as expected.

    >>> (
    ...     explanation
    ...     .groupby('year')
    ...     .apply(lambda x: (x.inner + x.mix).sum(), include_groups=False)
    ...     .rename('diff')
    ...     .reset_index()
    ... )
       year     diff
    0  2022  -924.25
    1  2023  1287.74

    """


def test_claims_with_gaps():
    """

    In practice, dimension values don't always appear for each period of time. It's good to check
    that the implementation can handle such cases.

    >>> import icanexplain as ice

    >>> claims = make_claims()
    >>> claims = claims.drop(index=claims.query('year == 2021 and claim_type == "Dentist"').index)
    >>> claims = claims.drop(index=claims.query('year == 2022 and claim_type == "Physiotherapy"').index)

    >>> (
    ...     claims
    ...     .groupby('year')
    ...     .agg({'amount': 'sum'})
    ...     .assign(diff=lambda x: x.amount.diff())
    ...     .reset_index()
    ... )
       year   amount     diff
    0  2021  2710.12      NaN
    1  2022  2550.84  -159.28
    2  2023  4178.03  1627.19

    >>> explainer = ice.SumExplainer(
    ...     fact='amount',
    ...     period='year',
    ...     group='claim_type'
    ... )
    >>> explanation = explainer(claims)
    >>> explanation
                                 inner          mix
    year claim_type
    2022 Dentist              0.000000   622.480000
         General Physician  -95.053333   249.693333
         Physiotherapy     -801.780000    -0.000000
         Psychiatrist      -282.030000   147.410000
    2023 Dentist            338.180000   480.330000
         General Physician  313.151429  -236.051429
         Physiotherapy        0.000000  1049.150000
         Psychiatrist       544.140000  -861.710000

    >>> (
    ...     explanation
    ...     .groupby('year')
    ...     .apply(lambda x: (x.inner + x.mix).sum(), include_groups=False)
    ...     .rename('diff')
    ...     .reset_index()
    ... )
       year     diff
    0  2022  -159.28
    1  2023  1627.19

    """


def test_agg_vs_samples():
    """

    We want to check that explanationing with a sample by sample approach gives the same results as
    explanationing with an aggregated table.

    >>> import icanexplain as ice

    >>> claims = make_claims()
    >>> (
    ...     claims
    ...     .groupby('year')
    ...     .agg({'amount': 'sum'})
    ...     .assign(diff=lambda x: x.amount.diff())
    ...     .reset_index()
    ... )
       year   amount     diff
    0  2021  3814.54      NaN
    1  2022  2890.29  -924.25
    2  2023  4178.03  1287.74

    Sample by sample.

    >>> explainer = ice.SumExplainer(
    ...     fact='amount',
    ...     period='year',
    ...     group='claim_type'
    ... )
    >>> explanation = explainer(claims)
    >>> explanation
                                 inner         mix
    year claim_type
    2022 Dentist           -170.700000 -311.240000
         General Physician  -95.053333  249.693333
         Physiotherapy     -122.880000 -339.450000
         Psychiatrist      -282.030000  147.410000
    2023 Dentist            338.180000  480.330000
         General Physician  313.151429 -236.051429
         Physiotherapy      185.125000  524.575000
         Psychiatrist       544.140000 -861.710000

    >>> (
    ...     explanation
    ...     .groupby('year')
    ...     .apply(lambda x: (x.inner + x.mix).sum(), include_groups=False)
    ...     .rename('diff')
    ...     .reset_index()
    ... )
       year     diff
    0  2022  -924.25
    1  2023  1287.74

    Aggregate.

    >>> claims_agg = (
    ...     claims
    ...     .groupby(['year', 'claim_type'])
    ...     ['amount'].agg(['mean', 'count'])
    ...     .reset_index()
    ... )
    >>> claims_agg
        year         claim_type        mean  count
    0   2021            Dentist  122.713333      9
    1   2021  General Physician   99.073333      6
    2   2021      Physiotherapy  133.630000      6
    3   2021       Psychiatrist  187.700000      7
    4   2022            Dentist  103.746667      6
    5   2022  General Physician   83.231111      9
    6   2022      Physiotherapy  113.150000      3
    7   2022       Psychiatrist  147.410000      8
    8   2023            Dentist  160.110000      9
    9   2023  General Physician  118.025714      7
    10  2023      Physiotherapy  174.858333      6
    11  2023       Psychiatrist  215.427500      4

    >>> explainer = ice.SumExplainer(
    ...     fact='mean',
    ...     period='year',
    ...     group='claim_type',
    ...     count='count'
    ... )
    >>> explanation = explainer(claims_agg)
    >>> explanation
                                 inner         mix
    year claim_type
    2022 Dentist           -170.700000 -311.240000
         General Physician  -95.053333  249.693333
         Physiotherapy     -122.880000 -339.450000
         Psychiatrist      -282.030000  147.410000
    2023 Dentist            338.180000  480.330000
         General Physician  313.151429 -236.051429
         Physiotherapy      185.125000  524.575000
         Psychiatrist       544.140000 -861.710000

    >>> (
    ...     explanation
    ...     .groupby('year')
    ...     .apply(lambda x: (x.inner + x.mix).sum(), include_groups=False)
    ...     .rename('diff')
    ...     .reset_index()
    ... )
       year     diff
    0  2022  -924.25
    1  2023  1287.74

    """
