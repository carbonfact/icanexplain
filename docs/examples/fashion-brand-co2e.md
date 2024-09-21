# Fashion brand CO2e emissions

Fashion brands increasingly have to be aware and report on their environmental footprint.

The following dataset comes from a real fashion brand, and has been anomamized. Each row represents a product manufactured in a given year.


```python
import icanexplain as ice

def fmt_CO2e(kg):
    if abs(kg) < 1e3:
        return f'{kg:,.1f}kgCO2e'
    return f'{kg / 1e6:,.1f}ktCO2e'

products = ice.datasets.load_product_footprints()
products.head(3).style.format({'footprint': fmt_CO2e, 'units': '{:,d}'})
```




<style type="text/css">
</style>
<table id="T_87d80">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_87d80_level0_col0" class="col_heading level0 col0" >year</th>
      <th id="T_87d80_level0_col1" class="col_heading level0 col1" >category</th>
      <th id="T_87d80_level0_col2" class="col_heading level0 col2" >product_id</th>
      <th id="T_87d80_level0_col3" class="col_heading level0 col3" >footprint</th>
      <th id="T_87d80_level0_col4" class="col_heading level0 col4" >units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_87d80_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_87d80_row0_col0" class="data row0 col0" >2021</td>
      <td id="T_87d80_row0_col1" class="data row0 col1" >DRESS</td>
      <td id="T_87d80_row0_col2" class="data row0 col2" >848be709</td>
      <td id="T_87d80_row0_col3" class="data row0 col3" >96.0kgCO2e</td>
      <td id="T_87d80_row0_col4" class="data row0 col4" >803</td>
    </tr>
    <tr>
      <th id="T_87d80_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_87d80_row1_col0" class="data row1 col0" >2021</td>
      <td id="T_87d80_row1_col1" class="data row1 col1" >DRESS</td>
      <td id="T_87d80_row1_col2" class="data row1 col2" >658f92b3</td>
      <td id="T_87d80_row1_col3" class="data row1 col3" >58.1kgCO2e</td>
      <td id="T_87d80_row1_col4" class="data row1 col4" >3,367</td>
    </tr>
    <tr>
      <th id="T_87d80_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_87d80_row2_col0" class="data row2 col0" >2021</td>
      <td id="T_87d80_row2_col1" class="data row2 col1" >DRESS</td>
      <td id="T_87d80_row2_col2" class="data row2 col2" >3a26f323</td>
      <td id="T_87d80_row2_col3" class="data row2 col3" >82.9kgCO2e</td>
      <td id="T_87d80_row2_col4" class="data row2 col4" >240</td>
    </tr>
  </tbody>
</table>




The `footprint` column indicates the product's carbon footprint in kgCO2e. The `units` column corresponds to the number of units produced.

Companies usually report their emissions on a yearly basis. We can do this by multiplying the footprint of each product by the number of units produced, and summing the results.


```python
(
    products
    .groupby('year')
    .apply(lambda g: (g['footprint'] * g['units']).sum() / g['units'].sum(), include_groups=False)
    .to_frame('average')
    .assign(diff=lambda x: x.average.diff())
    .style.format(fmt_CO2e, na_rep='')
)
```




<style type="text/css">
</style>
<table id="T_ecb7f">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_ecb7f_level0_col0" class="col_heading level0 col0" >average</th>
      <th id="T_ecb7f_level0_col1" class="col_heading level0 col1" >diff</th>
    </tr>
    <tr>
      <th class="index_name level0" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_ecb7f_level0_row0" class="row_heading level0 row0" >2021</th>
      <td id="T_ecb7f_row0_col0" class="data row0 col0" >22.0kgCO2e</td>
      <td id="T_ecb7f_row0_col1" class="data row0 col1" ></td>
    </tr>
    <tr>
      <th id="T_ecb7f_level0_row1" class="row_heading level0 row1" >2022</th>
      <td id="T_ecb7f_row1_col0" class="data row1 col0" >21.7kgCO2e</td>
      <td id="T_ecb7f_row1_col1" class="data row1 col1" >-0.2kgCO2e</td>
    </tr>
    <tr>
      <th id="T_ecb7f_level0_row2" class="row_heading level0 row2" >2023</th>
      <td id="T_ecb7f_row2_col0" class="data row2 col0" >22.7kgCO2e</td>
      <td id="T_ecb7f_row2_col1" class="data row2 col1" >1.0kgCO2e</td>
    </tr>
  </tbody>
</table>





```python
explainer = ice.MeanExplainer(
    fact='footprint',
    count='units',
    period='year',
    group='category',
)
explanation = explainer(products)
#explanation.style.format({'mean': fmt_CO2e, 'total': fmt_CO2e, 'inner': fmt_CO2e, 'mix': fmt_CO2e}, na_rep='')
explanation
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>inner</th>
      <th>mix</th>
    </tr>
    <tr>
      <th>year</th>
      <th>category</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="6" valign="top">2022</th>
      <th>DRESS</th>
      <td>0.047641</td>
      <td>-0.136117</td>
    </tr>
    <tr>
      <th>JACKET</th>
      <td>-0.165587</td>
      <td>-0.690534</td>
    </tr>
    <tr>
      <th>PANTS</th>
      <td>0.614527</td>
      <td>0.202821</td>
    </tr>
    <tr>
      <th>SHIRT</th>
      <td>-0.017933</td>
      <td>0.004249</td>
    </tr>
    <tr>
      <th>SWEATER</th>
      <td>-0.394262</td>
      <td>-0.088120</td>
    </tr>
    <tr>
      <th>TSHIRT</th>
      <td>0.084757</td>
      <td>0.301677</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">2023</th>
      <th>DRESS</th>
      <td>-0.081552</td>
      <td>0.512899</td>
    </tr>
    <tr>
      <th>JACKET</th>
      <td>-0.129072</td>
      <td>0.969850</td>
    </tr>
    <tr>
      <th>PANTS</th>
      <td>-0.218760</td>
      <td>-0.088232</td>
    </tr>
    <tr>
      <th>SHIRT</th>
      <td>0.017802</td>
      <td>-0.034301</td>
    </tr>
    <tr>
      <th>SWEATER</th>
      <td>-0.062852</td>
      <td>0.357931</td>
    </tr>
    <tr>
      <th>TSHIRT</th>
      <td>-0.162470</td>
      <td>-0.055981</td>
    </tr>
  </tbody>
</table>
</div>




```python
explanation.groupby('year').sum().sum(axis=1)
```




    year
    2022   -0.236879
    2023    1.025264
    dtype: float64



Here's the meaning of each column:

- `inner` is the difference due to the change in the average footprint per unit. A negative inner values means the footprint per unit shifted in a way that reduced emissions. For instance, low emission products seem to have been prioritized in 2022 (-17.5ktCO2e), but not in 2023 (+73.4ktCO2e).
- `mix` is the difference due to the change in the number of units produced. A negative mix value means the number of units produced shifted in a way that reduced emissions.

A convenient way to read these values is to use a waterfall chart.


```python
explainer.plot(products)
```





<style>
  #altair-viz-67f11986abc44bb5b28d56106ff594bf.vega-embed {
    width: 100%;
    display: flex;
  }

  #altair-viz-67f11986abc44bb5b28d56106ff594bf.vega-embed details,
  #altair-viz-67f11986abc44bb5b28d56106ff594bf.vega-embed details summary {
    position: relative;
  }
</style>
<div id="altair-viz-67f11986abc44bb5b28d56106ff594bf"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-67f11986abc44bb5b28d56106ff594bf") {
      outputDiv = document.getElementById("altair-viz-67f11986abc44bb5b28d56106ff594bf");
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
  })({"config": {"view": {"continuousWidth": 300, "continuousHeight": 300}}, "layer": [{"data": {"name": "data-242fb01f675a7449bfae6fe3be21401d"}, "mark": {"type": "bar"}, "encoding": {"tooltip": [{"field": "total", "type": "quantitative"}], "x": {"field": "total", "type": "quantitative"}, "y": {"field": "label", "sort": null, "type": "ordinal"}}, "name": "view_1"}, {"data": {"name": "data-0404f28059e953832bec1209b4f842bc"}, "mark": {"type": "bar"}, "encoding": {"color": {"field": "is_positive", "legend": null, "scale": {"domain": [true, false], "range": ["green", "red"]}, "type": "nominal"}, "tooltip": [{"field": "year", "type": "quantitative"}, {"field": "category", "type": "nominal"}, {"field": "kind", "type": "nominal"}, {"field": "impact", "type": "quantitative"}], "x": {"axis": {"title": "footprint"}, "field": "start", "type": "quantitative"}, "x2": {"field": "end"}, "y": {"axis": {"title": null}, "field": "label", "sort": null, "type": "ordinal"}}}, {"data": {"name": "data-fc12db6576e26917b3997c993f164d30"}, "mark": {"type": "bar"}, "encoding": {"tooltip": [{"field": "total", "type": "quantitative"}], "x": {"field": "total", "type": "quantitative"}, "y": {"field": "label", "sort": null, "type": "ordinal"}}}, {"data": {"name": "data-ebcd48c22dfff6f4059b7824a40fa780"}, "mark": {"type": "bar"}, "encoding": {"color": {"field": "is_positive", "legend": null, "scale": {"domain": [true, false], "range": ["green", "red"]}, "type": "nominal"}, "tooltip": [{"field": "year", "type": "quantitative"}, {"field": "category", "type": "nominal"}, {"field": "kind", "type": "nominal"}, {"field": "impact", "type": "quantitative"}], "x": {"axis": {"title": "footprint"}, "field": "start", "type": "quantitative"}, "x2": {"field": "end"}, "y": {"axis": {"title": null}, "field": "label", "sort": null, "type": "ordinal"}}}, {"data": {"name": "data-f28063f888fbd67e94d16ee44839474a"}, "mark": {"type": "bar"}, "encoding": {"tooltip": [{"field": "total", "type": "quantitative"}], "x": {"field": "total", "type": "quantitative"}, "y": {"field": "label", "sort": null, "type": "ordinal"}}}], "params": [{"name": "param_1", "select": {"type": "interval", "encodings": ["x", "y"]}, "bind": "scales", "views": ["view_1"]}], "$schema": "https://vega.github.io/schema/vega-lite/v5.17.0.json", "datasets": {"data-242fb01f675a7449bfae6fe3be21401d": [{"label": [2021], "total": 21.95027759780389}], "data-0404f28059e953832bec1209b4f842bc": [{"year": 2022, "category": "PANTS", "impact": 0.6145273388886315, "kind": "inner", "end": 22.56480493669252, "start": 21.95027759780389, "label": "2022 \u2022 PANTS \u2022 inner", "is_positive": true}, {"year": 2022, "category": "TSHIRT", "impact": 0.30167724893309866, "kind": "mix", "end": 22.86648218562562, "start": 22.56480493669252, "label": "2022 \u2022 TSHIRT \u2022 mix", "is_positive": true}, {"year": 2022, "category": "PANTS", "impact": 0.2028211345999768, "kind": "mix", "end": 23.069303320225597, "start": 22.86648218562562, "label": "2022 \u2022 PANTS \u2022 mix", "is_positive": true}, {"year": 2022, "category": "TSHIRT", "impact": 0.08475665867342684, "kind": "inner", "end": 23.154059978899024, "start": 23.069303320225597, "label": "2022 \u2022 TSHIRT \u2022 inner", "is_positive": true}, {"year": 2022, "category": "DRESS", "impact": 0.04764107525793142, "kind": "inner", "end": 23.201701054156956, "start": 23.154059978899024, "label": "2022 \u2022 DRESS \u2022 inner", "is_positive": true}, {"year": 2022, "category": "SHIRT", "impact": 0.004249415405470712, "kind": "mix", "end": 23.205950469562424, "start": 23.201701054156956, "label": "2022 \u2022 SHIRT \u2022 mix", "is_positive": true}, {"year": 2022, "category": "SHIRT", "impact": -0.017932535305564764, "kind": "inner", "end": 23.188017934256862, "start": 23.205950469562424, "label": "2022 \u2022 SHIRT \u2022 inner", "is_positive": false}, {"year": 2022, "category": "SWEATER", "impact": -0.08811989002715365, "kind": "mix", "end": 23.099898044229707, "start": 23.188017934256862, "label": "2022 \u2022 SWEATER \u2022 mix", "is_positive": false}, {"year": 2022, "category": "DRESS", "impact": -0.13611661127961636, "kind": "mix", "end": 22.963781432950093, "start": 23.099898044229707, "label": "2022 \u2022 DRESS \u2022 mix", "is_positive": false}, {"year": 2022, "category": "JACKET", "impact": -0.16558724703683306, "kind": "inner", "end": 22.798194185913257, "start": 22.963781432950093, "label": "2022 \u2022 JACKET \u2022 inner", "is_positive": false}, {"year": 2022, "category": "SWEATER", "impact": -0.39426152927404745, "kind": "inner", "end": 22.40393265663921, "start": 22.798194185913257, "label": "2022 \u2022 SWEATER \u2022 inner", "is_positive": false}, {"year": 2022, "category": "JACKET", "impact": -0.6905343501362712, "kind": "mix", "end": 21.71339830650294, "start": 22.40393265663921, "label": "2022 \u2022 JACKET \u2022 mix", "is_positive": false}], "data-fc12db6576e26917b3997c993f164d30": [{"label": [2022], "total": 21.713398306502945}], "data-ebcd48c22dfff6f4059b7824a40fa780": [{"year": 2023, "category": "JACKET", "impact": 0.9698501184475561, "kind": "mix", "end": 22.683248424950502, "start": 21.713398306502945, "label": "2023 \u2022 JACKET \u2022 mix", "is_positive": true}, {"year": 2023, "category": "DRESS", "impact": 0.5128989262972464, "kind": "mix", "end": 23.19614735124775, "start": 22.683248424950502, "label": "2023 \u2022 DRESS \u2022 mix", "is_positive": true}, {"year": 2023, "category": "SWEATER", "impact": 0.3579306618365037, "kind": "mix", "end": 23.55407801308425, "start": 23.19614735124775, "label": "2023 \u2022 SWEATER \u2022 mix", "is_positive": true}, {"year": 2023, "category": "SHIRT", "impact": 0.017802295811369558, "kind": "inner", "end": 23.571880308895622, "start": 23.55407801308425, "label": "2023 \u2022 SHIRT \u2022 inner", "is_positive": true}, {"year": 2023, "category": "SHIRT", "impact": -0.034300793942507526, "kind": "mix", "end": 23.537579514953112, "start": 23.571880308895622, "label": "2023 \u2022 SHIRT \u2022 mix", "is_positive": false}, {"year": 2023, "category": "TSHIRT", "impact": -0.05598069939020174, "kind": "mix", "end": 23.48159881556291, "start": 23.537579514953112, "label": "2023 \u2022 TSHIRT \u2022 mix", "is_positive": false}, {"year": 2023, "category": "SWEATER", "impact": -0.06285171538046565, "kind": "inner", "end": 23.418747100182447, "start": 23.48159881556291, "label": "2023 \u2022 SWEATER \u2022 inner", "is_positive": false}, {"year": 2023, "category": "DRESS", "impact": -0.08155163940547772, "kind": "inner", "end": 23.337195460776968, "start": 23.418747100182447, "label": "2023 \u2022 DRESS \u2022 inner", "is_positive": false}, {"year": 2023, "category": "PANTS", "impact": -0.08823155008199736, "kind": "mix", "end": 23.24896391069497, "start": 23.337195460776968, "label": "2023 \u2022 PANTS \u2022 mix", "is_positive": false}, {"year": 2023, "category": "JACKET", "impact": -0.12907195009877084, "kind": "inner", "end": 23.1198919605962, "start": 23.24896391069497, "label": "2023 \u2022 JACKET \u2022 inner", "is_positive": false}, {"year": 2023, "category": "TSHIRT", "impact": -0.16246975189864427, "kind": "inner", "end": 22.957422208697555, "start": 23.1198919605962, "label": "2023 \u2022 TSHIRT \u2022 inner", "is_positive": false}, {"year": 2023, "category": "PANTS", "impact": -0.21876005026772086, "kind": "inner", "end": 22.738662158429836, "start": 22.957422208697555, "label": "2023 \u2022 PANTS \u2022 inner", "is_positive": false}], "data-f28063f888fbd67e94d16ee44839474a": [{"label": [2023], "total": 22.738662158429833}]}}, {"mode": "vega-lite"});
</script>



This is better than reporting the average footprint and unit produced separately. It's more informative to quantify their contribution to the change in emissions. Here it's good to confirm that the decrease in emissions is mostly due to a reduction in the number of units produced for both years. But it's also good to see that there was an increase due to the average footprint in 2023. Importantly, each one of these effects is calculated, and not just assumed.

It's natural to want to deepen the analysis. For instance:

1. Why is there a significant inner contribution for pants in 2022? Is it because the materials are less sustainable? Or because the pants got heavier?
2. The reduction in 2023 is mainly due to the reduction in the number of units produced. Can this be broken down into marketing segments? For instance, is the reduction mainly driven by online or in-person sales? How does this break down by country?

These questions hint at the interactive aspect of this kind of analysis. Once you break down a metric's evolution along a dimension, the next steps are to break down the metric (question 1) and/or include another dimension (question 2).
