# Simple revenue funnel

We look at a toy website funnel in this example. Imagine a fictitious website that sells stuff. Users go to the website, are presented with items, can add them to their cart, and then can buy them.


```python
import pandas as pd
import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
def fmt_currency(x):
    return locale.currency(x, grouping=True)

traffic = pd.DataFrame({
    'date': ['2018-01-01', '2018-01-01', '2018-01-01', '2019-01-01', '2019-01-01', '2019-01-01', '2018-02-01', '2018-02-01', '2018-02-01', '2019-02-01', '2019-02-01', '2019-02-01'],
    'group': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'impressions': [1000, 2000, 2500, 1000, 2150, 2000, 50, 2000, 2500, 2500, 2150, 2000],
    'clicks': [150, 150, 250, 120, 200, 400, 20, 300, 250, 1000, 323, 320],
    'conversions': [120, 150, 125, 160, 145, 166, 10, 150, 125, 500, 145, 166],
    'revenue': ['$8,600', '$9,400', '$10,750', '$9,055', '$8,739', '$10,147', '$500', '$11,400', '$8,750', '$50,000', '$10,739', '$12,147'],
})
traffic['date'] = pd.to_datetime(traffic['date'])
traffic['revenue'] = traffic['revenue'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
traffic.style.format({'revenue': fmt_currency, 'date': lambda x: x.strftime('%Y-%m-%d')}, na_rep='N/A')
```




<style type="text/css">
</style>
<table id="T_aea2c">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_aea2c_level0_col0" class="col_heading level0 col0" >date</th>
      <th id="T_aea2c_level0_col1" class="col_heading level0 col1" >group</th>
      <th id="T_aea2c_level0_col2" class="col_heading level0 col2" >impressions</th>
      <th id="T_aea2c_level0_col3" class="col_heading level0 col3" >clicks</th>
      <th id="T_aea2c_level0_col4" class="col_heading level0 col4" >conversions</th>
      <th id="T_aea2c_level0_col5" class="col_heading level0 col5" >revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_aea2c_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_aea2c_row0_col0" class="data row0 col0" >2018-01-01</td>
      <td id="T_aea2c_row0_col1" class="data row0 col1" >A</td>
      <td id="T_aea2c_row0_col2" class="data row0 col2" >1000</td>
      <td id="T_aea2c_row0_col3" class="data row0 col3" >150</td>
      <td id="T_aea2c_row0_col4" class="data row0 col4" >120</td>
      <td id="T_aea2c_row0_col5" class="data row0 col5" >$8,600.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_aea2c_row1_col0" class="data row1 col0" >2018-01-01</td>
      <td id="T_aea2c_row1_col1" class="data row1 col1" >B</td>
      <td id="T_aea2c_row1_col2" class="data row1 col2" >2000</td>
      <td id="T_aea2c_row1_col3" class="data row1 col3" >150</td>
      <td id="T_aea2c_row1_col4" class="data row1 col4" >150</td>
      <td id="T_aea2c_row1_col5" class="data row1 col5" >$9,400.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_aea2c_row2_col0" class="data row2 col0" >2018-01-01</td>
      <td id="T_aea2c_row2_col1" class="data row2 col1" >C</td>
      <td id="T_aea2c_row2_col2" class="data row2 col2" >2500</td>
      <td id="T_aea2c_row2_col3" class="data row2 col3" >250</td>
      <td id="T_aea2c_row2_col4" class="data row2 col4" >125</td>
      <td id="T_aea2c_row2_col5" class="data row2 col5" >$10,750.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_aea2c_row3_col0" class="data row3 col0" >2019-01-01</td>
      <td id="T_aea2c_row3_col1" class="data row3 col1" >A</td>
      <td id="T_aea2c_row3_col2" class="data row3 col2" >1000</td>
      <td id="T_aea2c_row3_col3" class="data row3 col3" >120</td>
      <td id="T_aea2c_row3_col4" class="data row3 col4" >160</td>
      <td id="T_aea2c_row3_col5" class="data row3 col5" >$9,055.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_aea2c_row4_col0" class="data row4 col0" >2019-01-01</td>
      <td id="T_aea2c_row4_col1" class="data row4 col1" >B</td>
      <td id="T_aea2c_row4_col2" class="data row4 col2" >2150</td>
      <td id="T_aea2c_row4_col3" class="data row4 col3" >200</td>
      <td id="T_aea2c_row4_col4" class="data row4 col4" >145</td>
      <td id="T_aea2c_row4_col5" class="data row4 col5" >$8,739.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row5" class="row_heading level0 row5" >5</th>
      <td id="T_aea2c_row5_col0" class="data row5 col0" >2019-01-01</td>
      <td id="T_aea2c_row5_col1" class="data row5 col1" >C</td>
      <td id="T_aea2c_row5_col2" class="data row5 col2" >2000</td>
      <td id="T_aea2c_row5_col3" class="data row5 col3" >400</td>
      <td id="T_aea2c_row5_col4" class="data row5 col4" >166</td>
      <td id="T_aea2c_row5_col5" class="data row5 col5" >$10,147.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row6" class="row_heading level0 row6" >6</th>
      <td id="T_aea2c_row6_col0" class="data row6 col0" >2018-02-01</td>
      <td id="T_aea2c_row6_col1" class="data row6 col1" >A</td>
      <td id="T_aea2c_row6_col2" class="data row6 col2" >50</td>
      <td id="T_aea2c_row6_col3" class="data row6 col3" >20</td>
      <td id="T_aea2c_row6_col4" class="data row6 col4" >10</td>
      <td id="T_aea2c_row6_col5" class="data row6 col5" >$500.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row7" class="row_heading level0 row7" >7</th>
      <td id="T_aea2c_row7_col0" class="data row7 col0" >2018-02-01</td>
      <td id="T_aea2c_row7_col1" class="data row7 col1" >B</td>
      <td id="T_aea2c_row7_col2" class="data row7 col2" >2000</td>
      <td id="T_aea2c_row7_col3" class="data row7 col3" >300</td>
      <td id="T_aea2c_row7_col4" class="data row7 col4" >150</td>
      <td id="T_aea2c_row7_col5" class="data row7 col5" >$11,400.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row8" class="row_heading level0 row8" >8</th>
      <td id="T_aea2c_row8_col0" class="data row8 col0" >2018-02-01</td>
      <td id="T_aea2c_row8_col1" class="data row8 col1" >C</td>
      <td id="T_aea2c_row8_col2" class="data row8 col2" >2500</td>
      <td id="T_aea2c_row8_col3" class="data row8 col3" >250</td>
      <td id="T_aea2c_row8_col4" class="data row8 col4" >125</td>
      <td id="T_aea2c_row8_col5" class="data row8 col5" >$8,750.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row9" class="row_heading level0 row9" >9</th>
      <td id="T_aea2c_row9_col0" class="data row9 col0" >2019-02-01</td>
      <td id="T_aea2c_row9_col1" class="data row9 col1" >A</td>
      <td id="T_aea2c_row9_col2" class="data row9 col2" >2500</td>
      <td id="T_aea2c_row9_col3" class="data row9 col3" >1000</td>
      <td id="T_aea2c_row9_col4" class="data row9 col4" >500</td>
      <td id="T_aea2c_row9_col5" class="data row9 col5" >$50,000.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row10" class="row_heading level0 row10" >10</th>
      <td id="T_aea2c_row10_col0" class="data row10 col0" >2019-02-01</td>
      <td id="T_aea2c_row10_col1" class="data row10 col1" >B</td>
      <td id="T_aea2c_row10_col2" class="data row10 col2" >2150</td>
      <td id="T_aea2c_row10_col3" class="data row10 col3" >323</td>
      <td id="T_aea2c_row10_col4" class="data row10 col4" >145</td>
      <td id="T_aea2c_row10_col5" class="data row10 col5" >$10,739.00</td>
    </tr>
    <tr>
      <th id="T_aea2c_level0_row11" class="row_heading level0 row11" >11</th>
      <td id="T_aea2c_row11_col0" class="data row11 col0" >2019-02-01</td>
      <td id="T_aea2c_row11_col1" class="data row11 col1" >C</td>
      <td id="T_aea2c_row11_col2" class="data row11 col2" >2000</td>
      <td id="T_aea2c_row11_col3" class="data row11 col3" >320</td>
      <td id="T_aea2c_row11_col4" class="data row11 col4" >166</td>
      <td id="T_aea2c_row11_col5" class="data row11 col5" >$12,147.00</td>
    </tr>
  </tbody>
</table>




The users are bucketed into 3 groups: A, B, C. We've also bucketed impressions/clicks/conversions/revenue figures by month of the year.

We're interested in understanding how the metrics evolve over time. The basic method is to calculate each metric separately. To keep things simple, we can do this for each year.


```python
pd.DataFrame({
    'impressions': (
        traffic
        .assign(year=traffic.date.dt.year)
        .groupby('year')
        .impressions.sum()
    ),
    'click_rate': (
        traffic
        .assign(year=traffic.date.dt.year)
        .groupby('year')
        .apply(lambda x: x.clicks.sum() / x.impressions.sum(), include_groups=False)
    ),
    'conversion_rate': (
        traffic
        .assign(year=traffic.date.dt.year)
        .groupby('year')
        .apply(lambda x: x.conversions.sum() / x.clicks.sum(), include_groups=False)
    ),
    'average_spend': (
        traffic
        .assign(year=traffic.date.dt.year)
        .groupby('year')
        .apply(lambda x: x.revenue.sum() / x.conversions.sum(), include_groups=False)
    ),
    'revenue': (
        traffic
        .assign(year=traffic.date.dt.year)
        .groupby('year')
        .revenue.sum()
    )
}).style.format({'average_spend': fmt_currency, 'revenue': fmt_currency}, na_rep='')
```




<style type="text/css">
</style>
<table id="T_e28e2">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_e28e2_level0_col0" class="col_heading level0 col0" >impressions</th>
      <th id="T_e28e2_level0_col1" class="col_heading level0 col1" >click_rate</th>
      <th id="T_e28e2_level0_col2" class="col_heading level0 col2" >conversion_rate</th>
      <th id="T_e28e2_level0_col3" class="col_heading level0 col3" >average_spend</th>
      <th id="T_e28e2_level0_col4" class="col_heading level0 col4" >revenue</th>
    </tr>
    <tr>
      <th class="index_name level0" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_e28e2_level0_row0" class="row_heading level0 row0" >2018</th>
      <td id="T_e28e2_row0_col0" class="data row0 col0" >10050</td>
      <td id="T_e28e2_row0_col1" class="data row0 col1" >0.111443</td>
      <td id="T_e28e2_row0_col2" class="data row0 col2" >0.607143</td>
      <td id="T_e28e2_row0_col3" class="data row0 col3" >$72.65</td>
      <td id="T_e28e2_row0_col4" class="data row0 col4" >$49,400.00</td>
    </tr>
    <tr>
      <th id="T_e28e2_level0_row1" class="row_heading level0 row1" >2019</th>
      <td id="T_e28e2_row1_col0" class="data row1 col0" >11800</td>
      <td id="T_e28e2_row1_col1" class="data row1 col1" >0.200254</td>
      <td id="T_e28e2_row1_col2" class="data row1 col2" >0.542531</td>
      <td id="T_e28e2_row1_col3" class="data row1 col3" >$78.65</td>
      <td id="T_e28e2_row1_col4" class="data row1 col4" >$100,827.00</td>
    </tr>
  </tbody>
</table>




In and of itself, this is already quite interesting. However, what we really want to know is how the change of each metric contributes to the change in revenue. This is where icanexplain comes in.


```python
import icanexplain as ice

explainer = ice.FunnelExplainer(
    funnel=['impressions', 'clicks', 'conversions', 'revenue'],
    period='year',
    group=['month', 'group']
)
traffic = traffic.assign(
    month=traffic.date.dt.month,
    year=traffic.date.dt.year
)
explanation = explainer(traffic)
explanation.style.format(fmt_currency).set_properties(**{'text-align': 'right'})
```




<style type="text/css">
#T_7c395_row0_col0, #T_7c395_row0_col1, #T_7c395_row0_col2, #T_7c395_row0_col3, #T_7c395_row1_col0, #T_7c395_row1_col1, #T_7c395_row1_col2, #T_7c395_row1_col3, #T_7c395_row2_col0, #T_7c395_row2_col1, #T_7c395_row2_col2, #T_7c395_row2_col3, #T_7c395_row3_col0, #T_7c395_row3_col1, #T_7c395_row3_col2, #T_7c395_row3_col3, #T_7c395_row4_col0, #T_7c395_row4_col1, #T_7c395_row4_col2, #T_7c395_row4_col3, #T_7c395_row5_col0, #T_7c395_row5_col1, #T_7c395_row5_col2, #T_7c395_row5_col3 {
  text-align: right;
}
</style>
<table id="T_7c395">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_7c395_level0_col0" class="col_heading level0 col0" >impressions_contribution</th>
      <th id="T_7c395_level0_col1" class="col_heading level0 col1" >clicks_over_impressions_contribution</th>
      <th id="T_7c395_level0_col2" class="col_heading level0 col2" >conversions_over_clicks_contribution</th>
      <th id="T_7c395_level0_col3" class="col_heading level0 col3" >revenue_over_conversions_contribution</th>
    </tr>
    <tr>
      <th class="index_name level0" >year</th>
      <th class="index_name level1" >month</th>
      <th class="index_name level2" >group</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_7c395_level0_row0" class="row_heading level0 row0" rowspan="6">2019</th>
      <th id="T_7c395_level1_row0" class="row_heading level1 row0" rowspan="3">1</th>
      <th id="T_7c395_level2_row0" class="row_heading level2 row0" >A</th>
      <td id="T_7c395_row0_col0" class="data row0 col0" >$0.00</td>
      <td id="T_7c395_row0_col1" class="data row0 col1" >-$1,720.00</td>
      <td id="T_7c395_row0_col2" class="data row0 col2" >$4,586.67</td>
      <td id="T_7c395_row0_col3" class="data row0 col3" >-$2,411.67</td>
    </tr>
    <tr>
      <th id="T_7c395_level2_row1" class="row_heading level2 row1" >B</th>
      <td id="T_7c395_row1_col0" class="data row1 col0" >$705.00</td>
      <td id="T_7c395_row1_col1" class="data row1 col1" >$2,428.33</td>
      <td id="T_7c395_row1_col2" class="data row1 col2" >-$3,446.67</td>
      <td id="T_7c395_row1_col3" class="data row1 col3" >-$347.67</td>
    </tr>
    <tr>
      <th id="T_7c395_level2_row2" class="row_heading level2 row2" >C</th>
      <td id="T_7c395_row2_col0" class="data row2 col0" >-$2,150.00</td>
      <td id="T_7c395_row2_col1" class="data row2 col1" >$8,600.00</td>
      <td id="T_7c395_row2_col2" class="data row2 col2" >-$2,924.00</td>
      <td id="T_7c395_row2_col3" class="data row2 col3" >-$4,129.00</td>
    </tr>
    <tr>
      <th id="T_7c395_level1_row3" class="row_heading level1 row3" rowspan="3">2</th>
      <th id="T_7c395_level2_row3" class="row_heading level2 row3" >A</th>
      <td id="T_7c395_row3_col0" class="data row3 col0" >$24,500.00</td>
      <td id="T_7c395_row3_col1" class="data row3 col1" >$0.00</td>
      <td id="T_7c395_row3_col2" class="data row3 col2" >$0.00</td>
      <td id="T_7c395_row3_col3" class="data row3 col3" >$25,000.00</td>
    </tr>
    <tr>
      <th id="T_7c395_level2_row4" class="row_heading level2 row4" >B</th>
      <td id="T_7c395_row4_col0" class="data row4 col0" >$855.00</td>
      <td id="T_7c395_row4_col1" class="data row4 col1" >$19.00</td>
      <td id="T_7c395_row4_col2" class="data row4 col2" >-$1,254.00</td>
      <td id="T_7c395_row4_col3" class="data row4 col3" >-$281.00</td>
    </tr>
    <tr>
      <th id="T_7c395_level2_row5" class="row_heading level2 row5" >C</th>
      <td id="T_7c395_row5_col0" class="data row5 col0" >-$1,750.00</td>
      <td id="T_7c395_row5_col1" class="data row5 col1" >$4,200.00</td>
      <td id="T_7c395_row5_col2" class="data row5 col2" >$420.00</td>
      <td id="T_7c395_row5_col3" class="data row5 col3" >$527.00</td>
    </tr>
  </tbody>
</table>




This is powerful, because it allows us to understand the drivers of revenue growth. For example, between January 2018 and January 2019, revenue went up by $8,600 due an increase in clicks for group C. This is more insightful than just saying that their click rate went up.

One thing to keep in mind is that contributions sum up to the overall difference between two periods. This means that it's easy to unit test that the contributions are correct:


```python
(
    explanation
    .groupby('year').sum().sum(axis=1)
    .to_frame('sum')
    .style.format(fmt_currency)
)
```




<style type="text/css">
</style>
<table id="T_ee41b">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_ee41b_level0_col0" class="col_heading level0 col0" >sum</th>
    </tr>
    <tr>
      <th class="index_name level0" >year</th>
      <th class="blank col0" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ee41b_level0_row0" class="row_heading level0 row0" >2019</th>
      <td id="T_ee41b_row0_col0" class="data row0 col0" >$51,427.00</td>
    </tr>
  </tbody>
</table>




Of course, it would be more interesting to apply this methodology to some real data. One example is the [Google Analytics dataset sample](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset) which is publicly available in BigQuery. 
