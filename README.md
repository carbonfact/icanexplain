# icanexplain ~ explain why metrics change

This library is here to help with the difficult task of explaining why a metric changes. It's particularly useful for analysts, data scientists, analytics engineers, and business intelligence professionals who need to understand the drivers of a metric's change.

This README provides a small introduction. For more information, please refer to the [documentation](https://carbonfact.github.io/icanexplain).

Let's say you're an analyst at an Airbnb-like company. You're tasked with analyzing year-over-year revenue growth. You have obtained the following dataset:

```py
>>> import locale
>>> import pandas as pd
>>> _ = locale.setlocale(locale.LC_ALL, 'en_US')
>>> fmt_currency = lambda x: '' if pd.isna(x) else locale.currency(x, grouping=True)[:-3]

>>> revenue = pd.DataFrame.from_dict([
...     {'year': 2019, 'bookings': 1_000, 'revenue_per_booking': 200},
...     {'year': 2020, 'bookings': 1_000, 'revenue_per_booking': 220},
...     {'year': 2021, 'bookings': 1_500, 'revenue_per_booking': 220},
...     {'year': 2022, 'bookings': 1_700, 'revenue_per_booking': 225},
... ])
>>> (
...     revenue
...     .assign(bookings=revenue.bookings.apply('{:,d}'.format))
...     .assign(revenue_per_booking=revenue.revenue_per_booking.apply(fmt_currency))
...     .set_index('year')
... )
     bookings revenue_per_booking
year
2019    1,000                $200
2020    1,000                $220
2021    1,500                $220
2022    1,700                $225

```

It's quite straightforward to calculate the revenue for each year, and then to measure the year-over-year growth:

```py
>>> (
...     revenue
...     .assign(revenue=revenue.eval('bookings * revenue_per_booking'))
...     .assign(growth=lambda x: x.revenue.diff())
...     .assign(bookings=revenue.bookings.apply('{:,d}'.format))
...     .assign(revenue_per_booking=revenue.revenue_per_booking.apply(fmt_currency))
...     .assign(revenue=lambda x: x.revenue.apply(fmt_currency))
...     .assign(growth=lambda x: x.growth.apply(fmt_currency))
...     .set_index('year')
... )
     bookings revenue_per_booking   revenue    growth
year
2019    1,000                $200  $200,000
2020    1,000                $220  $220,000   $20,000
2021    1,500                $220  $330,000  $110,000
2022    1,700                $225  $382,500   $52,500

```

Growth can be due to two factors: an increase in the number of bookings, or an increase in the revenue per booking. The icanexplain library to decompose the growth into these two factors:

```py
>>> import icanexplain as ice
>>> explainer = ice.SumExplainer(
...     fact='revenue_per_booking',
...     period='year',
...     count='bookings'
... )
>>> explanation = explainer(revenue)
>>> explanation.map(fmt_currency)
        inner       mix
year
2020  $20,000        $0
2021       $0  $110,000
2022   $7,500   $45,000

```

Here's how to interpret this explanation:

- From 2019 to 2020, the revenue growth was entirely due to an increase in the revenue per booking. The number of bookings was exactly the same. Therefore, the $20,000 is entirely due to the inner effect (increase in revenue per booking).
- From 2020 to 2021, the revenue growth was entirely due to an increase in the number of bookings. The revenue per booking was exactly the same. Therefore, the $110,000 is entirely due to the mix effect (increase in bookings).
- From 2021 to 2022, there was a $52,500 revenue growth. However, the revenue per booking went down by $10, so the increase is due to the higher number of bookings. The inner effect is -$7,500 while the mix effect is $45,000.

Here's a visual representation of this last interpretation:

<div>
    <img src="https://github.com/user-attachments/assets/d93a8b33-929f-4895-87c8-1b60c8d3bb2f" alt="example" width="70%"/>
</div>
