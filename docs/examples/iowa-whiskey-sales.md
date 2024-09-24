# Iowa whiskey sales

Let's look at whiskey sales in Iowa. This is a subset of the data from the [Iowa Liquor Sales dataset](https://data.iowa.gov/Sales-Distribution/Iowa-Liquor-Sales/m3tr-qhgy).


```python
import icanexplain as ice

sales = ice.datasets.load_iowa_whiskey_sales()
sales.head().style.format()
```




<style type="text/css">
</style>
<table id="T_13ede">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_13ede_level0_col0" class="col_heading level0 col0" >date</th>
      <th id="T_13ede_level0_col1" class="col_heading level0 col1" >category</th>
      <th id="T_13ede_level0_col2" class="col_heading level0 col2" >vendor</th>
      <th id="T_13ede_level0_col3" class="col_heading level0 col3" >sales_amount</th>
      <th id="T_13ede_level0_col4" class="col_heading level0 col4" >price_per_bottle</th>
      <th id="T_13ede_level0_col5" class="col_heading level0 col5" >bottles_sold</th>
      <th id="T_13ede_level0_col6" class="col_heading level0 col6" >bottle_volume_ml</th>
      <th id="T_13ede_level0_col7" class="col_heading level0 col7" >year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_13ede_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_13ede_row0_col0" class="data row0 col0" >2012-06-04</td>
      <td id="T_13ede_row0_col1" class="data row0 col1" >CANADIAN WHISKIES</td>
      <td id="T_13ede_row0_col2" class="data row0 col2" >CONSTELLATION WINE COMPANY, INC.</td>
      <td id="T_13ede_row0_col3" class="data row0 col3" >94.020000</td>
      <td id="T_13ede_row0_col4" class="data row0 col4" >15.670000</td>
      <td id="T_13ede_row0_col5" class="data row0 col5" >6</td>
      <td id="T_13ede_row0_col6" class="data row0 col6" >1750</td>
      <td id="T_13ede_row0_col7" class="data row0 col7" >2012</td>
    </tr>
    <tr>
      <th id="T_13ede_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_13ede_row1_col0" class="data row1 col0" >2016-01-05</td>
      <td id="T_13ede_row1_col1" class="data row1 col1" >STRAIGHT BOURBON WHISKIES</td>
      <td id="T_13ede_row1_col2" class="data row1 col2" >CAMPARI(SKYY)</td>
      <td id="T_13ede_row1_col3" class="data row1 col3" >18.760000</td>
      <td id="T_13ede_row1_col4" class="data row1 col4" >9.380000</td>
      <td id="T_13ede_row1_col5" class="data row1 col5" >2</td>
      <td id="T_13ede_row1_col6" class="data row1 col6" >375</td>
      <td id="T_13ede_row1_col7" class="data row1 col7" >2016</td>
    </tr>
    <tr>
      <th id="T_13ede_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_13ede_row2_col0" class="data row2 col0" >2016-05-25</td>
      <td id="T_13ede_row2_col1" class="data row2 col1" >CANADIAN WHISKIES</td>
      <td id="T_13ede_row2_col2" class="data row2 col2" >DIAGEO AMERICAS</td>
      <td id="T_13ede_row2_col3" class="data row2 col3" >11.030000</td>
      <td id="T_13ede_row2_col4" class="data row2 col4" >11.030000</td>
      <td id="T_13ede_row2_col5" class="data row2 col5" >1</td>
      <td id="T_13ede_row2_col6" class="data row2 col6" >300</td>
      <td id="T_13ede_row2_col7" class="data row2 col7" >2016</td>
    </tr>
    <tr>
      <th id="T_13ede_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_13ede_row3_col0" class="data row3 col0" >2016-01-20</td>
      <td id="T_13ede_row3_col1" class="data row3 col1" >CANADIAN WHISKIES</td>
      <td id="T_13ede_row3_col2" class="data row3 col2" >PHILLIPS BEVERAGE COMPANY</td>
      <td id="T_13ede_row3_col3" class="data row3 col3" >33.840000</td>
      <td id="T_13ede_row3_col4" class="data row3 col4" >11.280000</td>
      <td id="T_13ede_row3_col5" class="data row3 col5" >3</td>
      <td id="T_13ede_row3_col6" class="data row3 col6" >750</td>
      <td id="T_13ede_row3_col7" class="data row3 col7" >2016</td>
    </tr>
    <tr>
      <th id="T_13ede_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_13ede_row4_col0" class="data row4 col0" >2012-03-19</td>
      <td id="T_13ede_row4_col1" class="data row4 col1" >CANADIAN WHISKIES</td>
      <td id="T_13ede_row4_col2" class="data row4 col2" >CONSTELLATION WINE COMPANY, INC.</td>
      <td id="T_13ede_row4_col3" class="data row4 col3" >94.020000</td>
      <td id="T_13ede_row4_col4" class="data row4 col4" >15.670000</td>
      <td id="T_13ede_row4_col5" class="data row4 col5" >6</td>
      <td id="T_13ede_row4_col6" class="data row4 col6" >1750</td>
      <td id="T_13ede_row4_col7" class="data row4 col7" >2012</td>
    </tr>
  </tbody>
</table>




The `sales_amount` column represents the bill a customer payed for a given transaction. We can sum it and group by year to see how the total sales amount evolves over time.


```python
import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
def fmt_currency(x):
    return locale.currency(x, grouping=True)

(
    sales.groupby('year')['sales_amount']
    .sum()
    .to_frame()
    .assign(diff=lambda x: x.diff())
    .style.format(lambda x: fmt_currency(x) if x > 0 else '')
)
```




<style type="text/css">
</style>
<table id="T_cd574">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_cd574_level0_col0" class="col_heading level0 col0" >sales_amount</th>
      <th id="T_cd574_level0_col1" class="col_heading level0 col1" >diff</th>
    </tr>
    <tr>
      <th class="index_name level0" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_cd574_level0_row0" class="row_heading level0 row0" >2012</th>
      <td id="T_cd574_row0_col0" class="data row0 col0" >$1,842,098.86</td>
      <td id="T_cd574_row0_col1" class="data row0 col1" ></td>
    </tr>
    <tr>
      <th id="T_cd574_level0_row1" class="row_heading level0 row1" >2016</th>
      <td id="T_cd574_row1_col0" class="data row1 col0" >$2,298,505.88</td>
      <td id="T_cd574_row1_col1" class="data row1 col1" >$456,407.02</td>
    </tr>
    <tr>
      <th id="T_cd574_level0_row2" class="row_heading level0 row2" >2020</th>
      <td id="T_cd574_row2_col0" class="data row2 col0" >$3,378,164.43</td>
      <td id="T_cd574_row2_col1" class="data row2 col1" >$1,079,658.55</td>
    </tr>
  </tbody>
</table>




Ok, but why? Well, we can use icanexplain to break down the evolution into two effects:

1. The inner effect: how much the average transaction value changed.
2. The mix effect: how much the number of transations changed.


```python
import icanexplain as ice

explainer = ice.SumExplainer(
    fact='sales_amount',
    period='year',
    group='category'
)
explanation = explainer(sales)
(
    explanation.style
    .format(lambda x: fmt_currency(x) if x > 0 else '$0')
    .set_properties(**{'text-align': 'right'})
)
```




<style type="text/css">
#T_1b403_row0_col0, #T_1b403_row0_col1, #T_1b403_row1_col0, #T_1b403_row1_col1, #T_1b403_row2_col0, #T_1b403_row2_col1, #T_1b403_row3_col0, #T_1b403_row3_col1, #T_1b403_row4_col0, #T_1b403_row4_col1, #T_1b403_row5_col0, #T_1b403_row5_col1, #T_1b403_row6_col0, #T_1b403_row6_col1, #T_1b403_row7_col0, #T_1b403_row7_col1, #T_1b403_row8_col0, #T_1b403_row8_col1, #T_1b403_row9_col0, #T_1b403_row9_col1, #T_1b403_row10_col0, #T_1b403_row10_col1, #T_1b403_row11_col0, #T_1b403_row11_col1, #T_1b403_row12_col0, #T_1b403_row12_col1, #T_1b403_row13_col0, #T_1b403_row13_col1, #T_1b403_row14_col0, #T_1b403_row14_col1, #T_1b403_row15_col0, #T_1b403_row15_col1 {
  text-align: right;
}
</style>
<table id="T_1b403">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_1b403_level0_col0" class="col_heading level0 col0" >inner</th>
      <th id="T_1b403_level0_col1" class="col_heading level0 col1" >mix</th>
    </tr>
    <tr>
      <th class="index_name level0" >year</th>
      <th class="index_name level1" >category</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_1b403_level0_row0" class="row_heading level0 row0" rowspan="8">2016</th>
      <th id="T_1b403_level1_row0" class="row_heading level1 row0" >BLENDED WHISKIES</th>
      <td id="T_1b403_row0_col0" class="data row0 col0" >$17,854.43</td>
      <td id="T_1b403_row0_col1" class="data row0 col1" >$7,356.77</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row1" class="row_heading level1 row1" >CANADIAN WHISKIES</th>
      <td id="T_1b403_row1_col0" class="data row1 col0" >$0</td>
      <td id="T_1b403_row1_col1" class="data row1 col1" >$225,902.66</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row2" class="row_heading level1 row2" >CORN WHISKIES</th>
      <td id="T_1b403_row2_col0" class="data row2 col0" >$0</td>
      <td id="T_1b403_row2_col1" class="data row2 col1" >$4,113.90</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row3" class="row_heading level1 row3" >IRISH WHISKIES</th>
      <td id="T_1b403_row3_col0" class="data row3 col0" >$22,144.48</td>
      <td id="T_1b403_row3_col1" class="data row3 col1" >$75,122.83</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row4" class="row_heading level1 row4" >SCOTCH WHISKIES</th>
      <td id="T_1b403_row4_col0" class="data row4 col0" >$19,591.97</td>
      <td id="T_1b403_row4_col1" class="data row4 col1" >$0</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row5" class="row_heading level1 row5" >SINGLE BARREL BOURBON WHISKIES</th>
      <td id="T_1b403_row5_col0" class="data row5 col0" >$1,852.03</td>
      <td id="T_1b403_row5_col1" class="data row5 col1" >$6,375.43</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row6" class="row_heading level1 row6" >STRAIGHT BOURBON WHISKIES</th>
      <td id="T_1b403_row6_col0" class="data row6 col0" >$107,144.93</td>
      <td id="T_1b403_row6_col1" class="data row6 col1" >$97,934.50</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row7" class="row_heading level1 row7" >STRAIGHT RYE WHISKIES</th>
      <td id="T_1b403_row7_col0" class="data row7 col0" >$0</td>
      <td id="T_1b403_row7_col1" class="data row7 col1" >$0</td>
    </tr>
    <tr>
      <th id="T_1b403_level0_row8" class="row_heading level0 row8" rowspan="8">2020</th>
      <th id="T_1b403_level1_row8" class="row_heading level1 row8" >BLENDED WHISKIES</th>
      <td id="T_1b403_row8_col0" class="data row8 col0" >$83,342.60</td>
      <td id="T_1b403_row8_col1" class="data row8 col1" >$59,768.58</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row9" class="row_heading level1 row9" >CANADIAN WHISKIES</th>
      <td id="T_1b403_row9_col0" class="data row9 col0" >$224,022.62</td>
      <td id="T_1b403_row9_col1" class="data row9 col1" >$149,363.35</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row10" class="row_heading level1 row10" >CORN WHISKIES</th>
      <td id="T_1b403_row10_col0" class="data row10 col0" >$1,517.48</td>
      <td id="T_1b403_row10_col1" class="data row10 col1" >$1,453.26</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row11" class="row_heading level1 row11" >IRISH WHISKIES</th>
      <td id="T_1b403_row11_col0" class="data row11 col0" >$0</td>
      <td id="T_1b403_row11_col1" class="data row11 col1" >$67,344.41</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row12" class="row_heading level1 row12" >SCOTCH WHISKIES</th>
      <td id="T_1b403_row12_col0" class="data row12 col0" >$19,840.48</td>
      <td id="T_1b403_row12_col1" class="data row12 col1" >$0</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row13" class="row_heading level1 row13" >SINGLE BARREL BOURBON WHISKIES</th>
      <td id="T_1b403_row13_col0" class="data row13 col0" >$11,958.32</td>
      <td id="T_1b403_row13_col1" class="data row13 col1" >$3,819.27</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row14" class="row_heading level1 row14" >STRAIGHT BOURBON WHISKIES</th>
      <td id="T_1b403_row14_col0" class="data row14 col0" >$167,864.46</td>
      <td id="T_1b403_row14_col1" class="data row14 col1" >$268,064.74</td>
    </tr>
    <tr>
      <th id="T_1b403_level1_row15" class="row_heading level1 row15" >STRAIGHT RYE WHISKIES</th>
      <td id="T_1b403_row15_col0" class="data row15 col0" >$0</td>
      <td id="T_1b403_row15_col1" class="data row15 col1" >$64,056.43</td>
    </tr>
  </tbody>
</table>




For instance, we see that the average transation amount for blended whiskies contributed to an $17,854 increase in sales from 2012 to 2016. This is the inner effect. The mix effect for blended whiskies, on the other hand, contributed to a $7,356 increase in sales.

Here's another example: the mix effect of Canadian whiskies is $225,902. This value, the mix effect, represents the increase due to the number of extra sales for Canadian whiskies. The inner effect, on the other hand, is $0. This means that the average transaction value for Canadian whiskies did not change between 2012 and 2016, and therefore didn't contribute to the increase in sales.

A visual way to look interpret the above table is to use a waterfall chart. The idea is that the contributions sum to the difference between two periods. In this case, the difference in sales from 2012 to 2016 is $456,407. The waterfall chart shows how the inner and mix effects contributed to this difference.


```python
explainer.plot(sales)
```





<style>
  #altair-viz-d41ef96cb7204817bd9f6ddd59db67d3.vega-embed {
    width: 100%;
    display: flex;
  }

  #altair-viz-d41ef96cb7204817bd9f6ddd59db67d3.vega-embed details,
  #altair-viz-d41ef96cb7204817bd9f6ddd59db67d3.vega-embed details summary {
    position: relative;
  }
</style>
<div id="altair-viz-d41ef96cb7204817bd9f6ddd59db67d3"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-d41ef96cb7204817bd9f6ddd59db67d3") {
      outputDiv = document.getElementById("altair-viz-d41ef96cb7204817bd9f6ddd59db67d3");
    }
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm/vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm/vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm/vega-lite@5.17.0?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm/vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "5.17.0"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 300, "continuousHeight": 300}}, "layer": [{"data": {"name": "data-2cde2fd109a6e9acf70d318feaf217e6"}, "mark": {"type": "bar"}, "encoding": {"tooltip": [{"field": "total", "type": "quantitative"}], "x": {"field": "total", "type": "quantitative"}, "y": {"field": "label", "sort": null, "type": "ordinal"}}, "name": "view_1"}, {"data": {"name": "data-a926bcfd3d5a579ed72e157f328d0558"}, "mark": {"type": "bar"}, "encoding": {"color": {"field": "is_positive", "legend": null, "scale": {"domain": [true, false], "range": ["green", "red"]}, "type": "nominal"}, "tooltip": [{"field": "year", "type": "quantitative"}, {"field": "category", "type": "nominal"}, {"field": "kind", "type": "nominal"}, {"field": "impact", "type": "quantitative"}], "x": {"axis": {"title": "sales_amount"}, "field": "start", "type": "quantitative"}, "x2": {"field": "end"}, "y": {"axis": {"title": null}, "field": "label", "sort": null, "type": "ordinal"}}}, {"data": {"name": "data-fcdb480df466db1be3744c58e3506c03"}, "mark": {"type": "bar"}, "encoding": {"tooltip": [{"field": "total", "type": "quantitative"}], "x": {"field": "total", "type": "quantitative"}, "y": {"field": "label", "sort": null, "type": "ordinal"}}}, {"data": {"name": "data-873356aecfdc388476ccee465bcbebef"}, "mark": {"type": "bar"}, "encoding": {"color": {"field": "is_positive", "legend": null, "scale": {"domain": [true, false], "range": ["green", "red"]}, "type": "nominal"}, "tooltip": [{"field": "year", "type": "quantitative"}, {"field": "category", "type": "nominal"}, {"field": "kind", "type": "nominal"}, {"field": "impact", "type": "quantitative"}], "x": {"axis": {"title": "sales_amount"}, "field": "start", "type": "quantitative"}, "x2": {"field": "end"}, "y": {"axis": {"title": null}, "field": "label", "sort": null, "type": "ordinal"}}}, {"data": {"name": "data-244c8da070240dcdf05dfddf0ad096fd"}, "mark": {"type": "bar"}, "encoding": {"tooltip": [{"field": "total", "type": "quantitative"}], "x": {"field": "total", "type": "quantitative"}, "y": {"field": "label", "sort": null, "type": "ordinal"}}}], "params": [{"name": "param_1", "select": {"type": "interval", "encodings": ["x", "y"]}, "bind": "scales", "views": ["view_1"]}], "$schema": "https://vega.github.io/schema/vega-lite/v5.17.0.json", "datasets": {"data-2cde2fd109a6e9acf70d318feaf217e6": [{"label": [2012], "total": 1842098.859999999}], "data-a926bcfd3d5a579ed72e157f328d0558": [{"year": 2016, "category": "CANADIAN WHISKIES", "impact": 225902.657725558, "kind": "mix", "end": 2068001.5177255569, "start": 1842098.859999999, "label": "2016 \u2022 CANADIAN WHISKIES \u2022 mix", "is_positive": true}, {"year": 2016, "category": "STRAIGHT BOURBON WHISKIES", "impact": 107144.93012664506, "kind": "inner", "end": 2175146.4478522018, "start": 2068001.5177255569, "label": "2016 \u2022 STRAIGHT BOURBON WHISKIES \u2022 inner", "is_positive": true}, {"year": 2016, "category": "STRAIGHT BOURBON WHISKIES", "impact": 97934.49987335323, "kind": "mix", "end": 2273080.9477255554, "start": 2175146.4478522018, "label": "2016 \u2022 STRAIGHT BOURBON WHISKIES \u2022 mix", "is_positive": true}, {"year": 2016, "category": "IRISH WHISKIES", "impact": 75122.82523437538, "kind": "mix", "end": 2348203.772959931, "start": 2273080.9477255554, "label": "2016 \u2022 IRISH WHISKIES \u2022 mix", "is_positive": true}, {"year": 2016, "category": "IRISH WHISKIES", "impact": 22144.48476562564, "kind": "inner", "end": 2370348.2577255564, "start": 2348203.772959931, "label": "2016 \u2022 IRISH WHISKIES \u2022 inner", "is_positive": true}, {"year": 2016, "category": "SCOTCH WHISKIES", "impact": 19591.969612402725, "kind": "inner", "end": 2389940.227337959, "start": 2370348.2577255564, "label": "2016 \u2022 SCOTCH WHISKIES \u2022 inner", "is_positive": true}, {"year": 2016, "category": "BLENDED WHISKIES", "impact": 17854.42684012496, "kind": "inner", "end": 2407794.654178084, "start": 2389940.227337959, "label": "2016 \u2022 BLENDED WHISKIES \u2022 inner", "is_positive": true}, {"year": 2016, "category": "BLENDED WHISKIES", "impact": 7356.77315987678, "kind": "mix", "end": 2415151.427337961, "start": 2407794.654178084, "label": "2016 \u2022 BLENDED WHISKIES \u2022 mix", "is_positive": true}, {"year": 2016, "category": "SINGLE BARREL BOURBON WHISKIES", "impact": 6375.427184466021, "kind": "mix", "end": 2421526.8545224266, "start": 2415151.427337961, "label": "2016 \u2022 SINGLE BARREL BOURBON WHISKIES \u2022 mix", "is_positive": true}, {"year": 2016, "category": "CORN WHISKIES", "impact": 4113.9000000000015, "kind": "mix", "end": 2425640.754522427, "start": 2421526.8545224266, "label": "2016 \u2022 CORN WHISKIES \u2022 mix", "is_positive": true}, {"year": 2016, "category": "SINGLE BARREL BOURBON WHISKIES", "impact": 1852.0328155339826, "kind": "inner", "end": 2427492.7873379607, "start": 2425640.754522427, "label": "2016 \u2022 SINGLE BARREL BOURBON WHISKIES \u2022 inner", "is_positive": true}, {"year": 2016, "category": "CORN WHISKIES", "impact": 0.0, "kind": "inner", "end": 2427492.7873379607, "start": 2427492.7873379607, "label": "2016 \u2022 CORN WHISKIES \u2022 inner", "is_positive": false}, {"year": 2016, "category": "SCOTCH WHISKIES", "impact": -13570.609612403085, "kind": "mix", "end": 2413922.1777255577, "start": 2427492.7873379607, "label": "2016 \u2022 SCOTCH WHISKIES \u2022 mix", "is_positive": false}, {"year": 2016, "category": "CANADIAN WHISKIES", "impact": -22278.517725560992, "kind": "inner", "end": 2391643.659999997, "start": 2413922.1777255577, "label": "2016 \u2022 CANADIAN WHISKIES \u2022 inner", "is_positive": false}, {"year": 2016, "category": "STRAIGHT RYE WHISKIES", "impact": -23929.320350877173, "kind": "inner", "end": 2367714.3396491194, "start": 2391643.659999997, "label": "2016 \u2022 STRAIGHT RYE WHISKIES \u2022 inner", "is_positive": false}, {"year": 2016, "category": "STRAIGHT RYE WHISKIES", "impact": -69208.45964912252, "kind": "mix", "end": 2298505.879999997, "start": 2367714.3396491194, "label": "2016 \u2022 STRAIGHT RYE WHISKIES \u2022 mix", "is_positive": false}], "data-fcdb480df466db1be3744c58e3506c03": [{"label": [2016], "total": 2298505.879999997}], "data-873356aecfdc388476ccee465bcbebef": [{"year": 2020, "category": "STRAIGHT BOURBON WHISKIES", "impact": 268064.7402925044, "kind": "mix", "end": 2566570.6202925015, "start": 2298505.879999997, "label": "2020 \u2022 STRAIGHT BOURBON WHISKIES \u2022 mix", "is_positive": true}, {"year": 2020, "category": "CANADIAN WHISKIES", "impact": 224022.61605993344, "kind": "inner", "end": 2790593.236352435, "start": 2566570.6202925015, "label": "2020 \u2022 CANADIAN WHISKIES \u2022 inner", "is_positive": true}, {"year": 2020, "category": "STRAIGHT BOURBON WHISKIES", "impact": 167864.45970749695, "kind": "inner", "end": 2958457.696059932, "start": 2790593.236352435, "label": "2020 \u2022 STRAIGHT BOURBON WHISKIES \u2022 inner", "is_positive": true}, {"year": 2020, "category": "CANADIAN WHISKIES", "impact": 149363.35394006473, "kind": "mix", "end": 3107821.0499999966, "start": 2958457.696059932, "label": "2020 \u2022 CANADIAN WHISKIES \u2022 mix", "is_positive": true}, {"year": 2020, "category": "BLENDED WHISKIES", "impact": 83342.5971874109, "kind": "inner", "end": 3191163.6471874076, "start": 3107821.0499999966, "label": "2020 \u2022 BLENDED WHISKIES \u2022 inner", "is_positive": true}, {"year": 2020, "category": "IRISH WHISKIES", "impact": 67344.40679665783, "kind": "mix", "end": 3258508.0539840655, "start": 3191163.6471874076, "label": "2020 \u2022 IRISH WHISKIES \u2022 mix", "is_positive": true}, {"year": 2020, "category": "STRAIGHT RYE WHISKIES", "impact": 64056.431595091875, "kind": "mix", "end": 3322564.4855791572, "start": 3258508.0539840655, "label": "2020 \u2022 STRAIGHT RYE WHISKIES \u2022 mix", "is_positive": true}, {"year": 2020, "category": "BLENDED WHISKIES", "impact": 59768.5828125906, "kind": "mix", "end": 3382333.068391748, "start": 3322564.4855791572, "label": "2020 \u2022 BLENDED WHISKIES \u2022 mix", "is_positive": true}, {"year": 2020, "category": "SCOTCH WHISKIES", "impact": 19840.47750433307, "kind": "inner", "end": 3402173.545896081, "start": 3382333.068391748, "label": "2020 \u2022 SCOTCH WHISKIES \u2022 inner", "is_positive": true}, {"year": 2020, "category": "SINGLE BARREL BOURBON WHISKIES", "impact": 11958.31739495796, "kind": "inner", "end": 3414131.8632910387, "start": 3402173.545896081, "label": "2020 \u2022 SINGLE BARREL BOURBON WHISKIES \u2022 inner", "is_positive": true}, {"year": 2020, "category": "SINGLE BARREL BOURBON WHISKIES", "impact": 3819.2726050420133, "kind": "mix", "end": 3417951.1358960806, "start": 3414131.8632910387, "label": "2020 \u2022 SINGLE BARREL BOURBON WHISKIES \u2022 mix", "is_positive": true}, {"year": 2020, "category": "CORN WHISKIES", "impact": 1517.4805128205116, "kind": "inner", "end": 3419468.6164089013, "start": 3417951.1358960806, "label": "2020 \u2022 CORN WHISKIES \u2022 inner", "is_positive": true}, {"year": 2020, "category": "CORN WHISKIES", "impact": 1453.2594871794872, "kind": "mix", "end": 3420921.8758960804, "start": 3419468.6164089013, "label": "2020 \u2022 CORN WHISKIES \u2022 mix", "is_positive": true}, {"year": 2020, "category": "STRAIGHT RYE WHISKIES", "impact": -9839.091595091852, "kind": "inner", "end": 3411082.7843009885, "start": 3420921.8758960804, "label": "2020 \u2022 STRAIGHT RYE WHISKIES \u2022 inner", "is_positive": false}, {"year": 2020, "category": "IRISH WHISKIES", "impact": -14048.436796657195, "kind": "inner", "end": 3397034.3475043317, "start": 3411082.7843009885, "label": "2020 \u2022 IRISH WHISKIES \u2022 inner", "is_positive": false}, {"year": 2020, "category": "SCOTCH WHISKIES", "impact": -18869.91750433277, "kind": "mix", "end": 3378164.429999999, "start": 3397034.3475043317, "label": "2020 \u2022 SCOTCH WHISKIES \u2022 mix", "is_positive": false}], "data-244c8da070240dcdf05dfddf0ad096fd": [{"label": [2020], "total": 3378164.4299999992}]}}, {"mode": "vega-lite"});
</script>


