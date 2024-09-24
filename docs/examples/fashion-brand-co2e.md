# Fashion brand CO2e emissions

Fashion brands increasingly have to be aware and report on their environmental footprint.

The following dataset comes from a real fashion brand, and has been anomymized. Each row represents a product manufactured in a given year.


```python
import icanexplain as ice

def fmt_CO2e(kg):
    if abs(kg) < 1e3:
        return f'{kg:,.2f}kgCO2e'
    return f'{kg / 1e6:,.1f}ktCO2e'

products = ice.datasets.load_product_footprints()
products.sample(5).style.format({'footprint': fmt_CO2e, 'units': '{:,d}'})
```




<style type="text/css">
</style>
<table id="T_9e921">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_9e921_level0_col0" class="col_heading level0 col0" >year</th>
      <th id="T_9e921_level0_col1" class="col_heading level0 col1" >category</th>
      <th id="T_9e921_level0_col2" class="col_heading level0 col2" >product_id</th>
      <th id="T_9e921_level0_col3" class="col_heading level0 col3" >footprint</th>
      <th id="T_9e921_level0_col4" class="col_heading level0 col4" >units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_9e921_level0_row0" class="row_heading level0 row0" >37741</th>
      <td id="T_9e921_row0_col0" class="data row0 col0" >2021</td>
      <td id="T_9e921_row0_col1" class="data row0 col1" >TSHIRT</td>
      <td id="T_9e921_row0_col2" class="data row0 col2" >7d3babe0</td>
      <td id="T_9e921_row0_col3" class="data row0 col3" >8.81kgCO2e</td>
      <td id="T_9e921_row0_col4" class="data row0 col4" >17</td>
    </tr>
    <tr>
      <th id="T_9e921_level0_row1" class="row_heading level0 row1" >13568</th>
      <td id="T_9e921_row1_col0" class="data row1 col0" >2021</td>
      <td id="T_9e921_row1_col1" class="data row1 col1" >PANTS</td>
      <td id="T_9e921_row1_col2" class="data row1 col2" >9bcf3ca9</td>
      <td id="T_9e921_row1_col3" class="data row1 col3" >19.73kgCO2e</td>
      <td id="T_9e921_row1_col4" class="data row1 col4" >173</td>
    </tr>
    <tr>
      <th id="T_9e921_level0_row2" class="row_heading level0 row2" >24840</th>
      <td id="T_9e921_row2_col0" class="data row2 col0" >2021</td>
      <td id="T_9e921_row2_col1" class="data row2 col1" >PANTS</td>
      <td id="T_9e921_row2_col2" class="data row2 col2" >d6269b7a</td>
      <td id="T_9e921_row2_col3" class="data row2 col3" >38.71kgCO2e</td>
      <td id="T_9e921_row2_col4" class="data row2 col4" >95</td>
    </tr>
    <tr>
      <th id="T_9e921_level0_row3" class="row_heading level0 row3" >27264</th>
      <td id="T_9e921_row3_col0" class="data row3 col0" >2021</td>
      <td id="T_9e921_row3_col1" class="data row3 col1" >SHIRT</td>
      <td id="T_9e921_row3_col2" class="data row3 col2" >4b38bf02</td>
      <td id="T_9e921_row3_col3" class="data row3 col3" >5.24kgCO2e</td>
      <td id="T_9e921_row3_col4" class="data row3 col4" >1</td>
    </tr>
    <tr>
      <th id="T_9e921_level0_row4" class="row_heading level0 row4" >26246</th>
      <td id="T_9e921_row4_col0" class="data row4 col0" >2021</td>
      <td id="T_9e921_row4_col1" class="data row4 col1" >PANTS</td>
      <td id="T_9e921_row4_col2" class="data row4 col2" >6ad52115</td>
      <td id="T_9e921_row4_col3" class="data row4 col3" >54.74kgCO2e</td>
      <td id="T_9e921_row4_col4" class="data row4 col4" >3,631</td>
    </tr>
  </tbody>
</table>




The `footprint` column indicates the product's carbon footprint in kgCO2e. The `units` column corresponds to the number of units produced.

Companies usually report their emissions on a yearly basis. We can do this by multiplying the footprint of each product, with the number of units produced, and summing the results.


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
<table id="T_a3774">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_a3774_level0_col0" class="col_heading level0 col0" >average</th>
      <th id="T_a3774_level0_col1" class="col_heading level0 col1" >diff</th>
    </tr>
    <tr>
      <th class="index_name level0" >year</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_a3774_level0_row0" class="row_heading level0 row0" >2021</th>
      <td id="T_a3774_row0_col0" class="data row0 col0" >21.95kgCO2e</td>
      <td id="T_a3774_row0_col1" class="data row0 col1" ></td>
    </tr>
    <tr>
      <th id="T_a3774_level0_row1" class="row_heading level0 row1" >2022</th>
      <td id="T_a3774_row1_col0" class="data row1 col0" >21.71kgCO2e</td>
      <td id="T_a3774_row1_col1" class="data row1 col1" >-0.24kgCO2e</td>
    </tr>
    <tr>
      <th id="T_a3774_level0_row2" class="row_heading level0 row2" >2023</th>
      <td id="T_a3774_row2_col0" class="data row2 col0" >22.74kgCO2e</td>
      <td id="T_a3774_row2_col1" class="data row2 col1" >1.03kgCO2e</td>
    </tr>
  </tbody>
</table>




The average footprint went down between 2021 and 2022. It then went back up in 2023. Of course, we want to understand why. When they see this, fashion brands have one word coming out of their mouth: why, why, why?

The overall average footprint can change for two reasons:

1. The average footprint per product category evolved.
2. The mix of product categories evolved.

The second reason is called the *mix effect*. For instance, let's say t-shirts have a lower footprint than jackets. If the share of jackets produced in 2023 is higher than in 2022, the average footprint will go up.

The jackets in 2023 aren't necessarily the same than those of 2022. They could be more sustainable, and have a lower footprint. This is the tricky part: we need to disentangle the mix effect from the evolution of the footprint of each product category. That is the value proposition of this package.


```python
explainer = ice.MeanExplainer(
    fact='footprint',
    count='units',
    period='year',
    group='category',
)
explanation = explainer(products)
explanation.style.format({'inner': fmt_CO2e, 'mix': fmt_CO2e}, na_rep='')
```




<style type="text/css">
</style>
<table id="T_5997e">
  <thead>
    <tr>
      <th class="blank" >&nbsp;</th>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_5997e_level0_col0" class="col_heading level0 col0" >inner</th>
      <th id="T_5997e_level0_col1" class="col_heading level0 col1" >mix</th>
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
      <th id="T_5997e_level0_row0" class="row_heading level0 row0" rowspan="6">2022</th>
      <th id="T_5997e_level1_row0" class="row_heading level1 row0" >DRESS</th>
      <td id="T_5997e_row0_col0" class="data row0 col0" >0.05kgCO2e</td>
      <td id="T_5997e_row0_col1" class="data row0 col1" >-0.14kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row1" class="row_heading level1 row1" >JACKET</th>
      <td id="T_5997e_row1_col0" class="data row1 col0" >-0.17kgCO2e</td>
      <td id="T_5997e_row1_col1" class="data row1 col1" >-0.69kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row2" class="row_heading level1 row2" >PANTS</th>
      <td id="T_5997e_row2_col0" class="data row2 col0" >0.61kgCO2e</td>
      <td id="T_5997e_row2_col1" class="data row2 col1" >0.20kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row3" class="row_heading level1 row3" >SHIRT</th>
      <td id="T_5997e_row3_col0" class="data row3 col0" >-0.02kgCO2e</td>
      <td id="T_5997e_row3_col1" class="data row3 col1" >0.00kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row4" class="row_heading level1 row4" >SWEATER</th>
      <td id="T_5997e_row4_col0" class="data row4 col0" >-0.39kgCO2e</td>
      <td id="T_5997e_row4_col1" class="data row4 col1" >-0.09kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row5" class="row_heading level1 row5" >TSHIRT</th>
      <td id="T_5997e_row5_col0" class="data row5 col0" >0.08kgCO2e</td>
      <td id="T_5997e_row5_col1" class="data row5 col1" >0.30kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level0_row6" class="row_heading level0 row6" rowspan="6">2023</th>
      <th id="T_5997e_level1_row6" class="row_heading level1 row6" >DRESS</th>
      <td id="T_5997e_row6_col0" class="data row6 col0" >-0.08kgCO2e</td>
      <td id="T_5997e_row6_col1" class="data row6 col1" >0.51kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row7" class="row_heading level1 row7" >JACKET</th>
      <td id="T_5997e_row7_col0" class="data row7 col0" >-0.13kgCO2e</td>
      <td id="T_5997e_row7_col1" class="data row7 col1" >0.97kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row8" class="row_heading level1 row8" >PANTS</th>
      <td id="T_5997e_row8_col0" class="data row8 col0" >-0.22kgCO2e</td>
      <td id="T_5997e_row8_col1" class="data row8 col1" >-0.09kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row9" class="row_heading level1 row9" >SHIRT</th>
      <td id="T_5997e_row9_col0" class="data row9 col0" >0.02kgCO2e</td>
      <td id="T_5997e_row9_col1" class="data row9 col1" >-0.03kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row10" class="row_heading level1 row10" >SWEATER</th>
      <td id="T_5997e_row10_col0" class="data row10 col0" >-0.06kgCO2e</td>
      <td id="T_5997e_row10_col1" class="data row10 col1" >0.36kgCO2e</td>
    </tr>
    <tr>
      <th id="T_5997e_level1_row11" class="row_heading level1 row11" >TSHIRT</th>
      <td id="T_5997e_row11_col0" class="data row11 col0" >-0.16kgCO2e</td>
      <td id="T_5997e_row11_col1" class="data row11 col1" >-0.06kgCO2e</td>
    </tr>
  </tbody>
</table>




Here's the meaning of each column:

- `inner` is the difference due to the change in the average footprint per unit. A negative inner values means the footprint per unit shifted in a way that reduced emissions. For instance, low emission products seem to have been prioritized in 2022 (-17.5ktCO2e), but not in 2023 (+73.4ktCO2e).
- `mix` is the difference due to the change in the number of units produced. A negative mix value means the number of units produced shifted in a way that reduced emissions.

A convenient way to read these values is to use a waterfall chart.


```python
explainer.plot(products)
```





<style>
  #altair-viz-d0fde62ff3fd4a05ad196280ef0c354c.vega-embed {
    width: 100%;
    display: flex;
  }

  #altair-viz-d0fde62ff3fd4a05ad196280ef0c354c.vega-embed details,
  #altair-viz-d0fde62ff3fd4a05ad196280ef0c354c.vega-embed details summary {
    position: relative;
  }
</style>
<div id="altair-viz-d0fde62ff3fd4a05ad196280ef0c354c"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-d0fde62ff3fd4a05ad196280ef0c354c") {
      outputDiv = document.getElementById("altair-viz-d0fde62ff3fd4a05ad196280ef0c354c");
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
  })({"config": {"view": {"continuousWidth": 300, "continuousHeight": 300}}, "layer": [{"data": {"name": "data-f17017973b43150b484325aa9e82daa8"}, "mark": {"type": "bar"}, "encoding": {"tooltip": [{"field": "total", "type": "quantitative"}], "x": {"field": "total", "type": "quantitative"}, "y": {"field": "label", "sort": null, "type": "ordinal"}}, "name": "view_1"}, {"data": {"name": "data-b9fee22a8811f62f8e802bc86220e939"}, "mark": {"type": "bar"}, "encoding": {"color": {"field": "is_positive", "legend": null, "scale": {"domain": [true, false], "range": ["green", "red"]}, "type": "nominal"}, "tooltip": [{"field": "year", "type": "quantitative"}, {"field": "category", "type": "nominal"}, {"field": "kind", "type": "nominal"}, {"field": "impact", "type": "quantitative"}], "x": {"axis": {"title": "footprint"}, "field": "start", "type": "quantitative"}, "x2": {"field": "end"}, "y": {"axis": {"title": null}, "field": "label", "sort": null, "type": "ordinal"}}}, {"data": {"name": "data-bc638dec2a34df2f2471c7665833fe5f"}, "mark": {"type": "bar"}, "encoding": {"tooltip": [{"field": "total", "type": "quantitative"}], "x": {"field": "total", "type": "quantitative"}, "y": {"field": "label", "sort": null, "type": "ordinal"}}}, {"data": {"name": "data-238ce6794be2b25387e2bda94e764c49"}, "mark": {"type": "bar"}, "encoding": {"color": {"field": "is_positive", "legend": null, "scale": {"domain": [true, false], "range": ["green", "red"]}, "type": "nominal"}, "tooltip": [{"field": "year", "type": "quantitative"}, {"field": "category", "type": "nominal"}, {"field": "kind", "type": "nominal"}, {"field": "impact", "type": "quantitative"}], "x": {"axis": {"title": "footprint"}, "field": "start", "type": "quantitative"}, "x2": {"field": "end"}, "y": {"axis": {"title": null}, "field": "label", "sort": null, "type": "ordinal"}}}, {"data": {"name": "data-f28063f888fbd67e94d16ee44839474a"}, "mark": {"type": "bar"}, "encoding": {"tooltip": [{"field": "total", "type": "quantitative"}], "x": {"field": "total", "type": "quantitative"}, "y": {"field": "label", "sort": null, "type": "ordinal"}}}], "params": [{"name": "param_1", "select": {"type": "interval", "encodings": ["x", "y"]}, "bind": "scales", "views": ["view_1"]}], "$schema": "https://vega.github.io/schema/vega-lite/v5.17.0.json", "datasets": {"data-f17017973b43150b484325aa9e82daa8": [{"label": [2021], "total": 21.950277597803893}], "data-b9fee22a8811f62f8e802bc86220e939": [{"year": 2022, "category": "PANTS", "impact": 0.6145273388886315, "kind": "inner", "end": 22.564804936692525, "start": 21.950277597803893, "label": "2022 \u2022 PANTS \u2022 inner", "is_positive": true}, {"year": 2022, "category": "TSHIRT", "impact": 0.30167724893309866, "kind": "mix", "end": 22.866482185625625, "start": 22.564804936692525, "label": "2022 \u2022 TSHIRT \u2022 mix", "is_positive": true}, {"year": 2022, "category": "PANTS", "impact": 0.2028211345999768, "kind": "mix", "end": 23.0693033202256, "start": 22.866482185625625, "label": "2022 \u2022 PANTS \u2022 mix", "is_positive": true}, {"year": 2022, "category": "TSHIRT", "impact": 0.08475665867342684, "kind": "inner", "end": 23.154059978899028, "start": 23.0693033202256, "label": "2022 \u2022 TSHIRT \u2022 inner", "is_positive": true}, {"year": 2022, "category": "DRESS", "impact": 0.04764107525793142, "kind": "inner", "end": 23.20170105415696, "start": 23.154059978899028, "label": "2022 \u2022 DRESS \u2022 inner", "is_positive": true}, {"year": 2022, "category": "SHIRT", "impact": 0.004249415405470712, "kind": "mix", "end": 23.205950469562428, "start": 23.20170105415696, "label": "2022 \u2022 SHIRT \u2022 mix", "is_positive": true}, {"year": 2022, "category": "SHIRT", "impact": -0.017932535305564764, "kind": "inner", "end": 23.188017934256866, "start": 23.205950469562428, "label": "2022 \u2022 SHIRT \u2022 inner", "is_positive": false}, {"year": 2022, "category": "SWEATER", "impact": -0.08811989002715365, "kind": "mix", "end": 23.09989804422971, "start": 23.188017934256866, "label": "2022 \u2022 SWEATER \u2022 mix", "is_positive": false}, {"year": 2022, "category": "DRESS", "impact": -0.13611661127961636, "kind": "mix", "end": 22.963781432950093, "start": 23.09989804422971, "label": "2022 \u2022 DRESS \u2022 mix", "is_positive": false}, {"year": 2022, "category": "JACKET", "impact": -0.16558724703683306, "kind": "inner", "end": 22.79819418591326, "start": 22.963781432950093, "label": "2022 \u2022 JACKET \u2022 inner", "is_positive": false}, {"year": 2022, "category": "SWEATER", "impact": -0.39426152927404745, "kind": "inner", "end": 22.403932656639213, "start": 22.79819418591326, "label": "2022 \u2022 SWEATER \u2022 inner", "is_positive": false}, {"year": 2022, "category": "JACKET", "impact": -0.6905343501362712, "kind": "mix", "end": 21.713398306502942, "start": 22.403932656639213, "label": "2022 \u2022 JACKET \u2022 mix", "is_positive": false}], "data-bc638dec2a34df2f2471c7665833fe5f": [{"label": [2022], "total": 21.713398306502942}], "data-238ce6794be2b25387e2bda94e764c49": [{"year": 2023, "category": "JACKET", "impact": 0.9698501184475561, "kind": "mix", "end": 22.6832484249505, "start": 21.713398306502942, "label": "2023 \u2022 JACKET \u2022 mix", "is_positive": true}, {"year": 2023, "category": "DRESS", "impact": 0.5128989262972464, "kind": "mix", "end": 23.196147351247745, "start": 22.6832484249505, "label": "2023 \u2022 DRESS \u2022 mix", "is_positive": true}, {"year": 2023, "category": "SWEATER", "impact": 0.3579306618365037, "kind": "mix", "end": 23.554078013084247, "start": 23.196147351247745, "label": "2023 \u2022 SWEATER \u2022 mix", "is_positive": true}, {"year": 2023, "category": "SHIRT", "impact": 0.017802295811369558, "kind": "inner", "end": 23.57188030889562, "start": 23.554078013084247, "label": "2023 \u2022 SHIRT \u2022 inner", "is_positive": true}, {"year": 2023, "category": "SHIRT", "impact": -0.034300793942507526, "kind": "mix", "end": 23.53757951495311, "start": 23.57188030889562, "label": "2023 \u2022 SHIRT \u2022 mix", "is_positive": false}, {"year": 2023, "category": "TSHIRT", "impact": -0.05598069939020174, "kind": "mix", "end": 23.481598815562908, "start": 23.53757951495311, "label": "2023 \u2022 TSHIRT \u2022 mix", "is_positive": false}, {"year": 2023, "category": "SWEATER", "impact": -0.06285171538046565, "kind": "inner", "end": 23.418747100182443, "start": 23.481598815562908, "label": "2023 \u2022 SWEATER \u2022 inner", "is_positive": false}, {"year": 2023, "category": "DRESS", "impact": -0.08155163940547772, "kind": "inner", "end": 23.337195460776964, "start": 23.418747100182443, "label": "2023 \u2022 DRESS \u2022 inner", "is_positive": false}, {"year": 2023, "category": "PANTS", "impact": -0.08823155008199736, "kind": "mix", "end": 23.248963910694968, "start": 23.337195460776964, "label": "2023 \u2022 PANTS \u2022 mix", "is_positive": false}, {"year": 2023, "category": "JACKET", "impact": -0.12907195009877084, "kind": "inner", "end": 23.119891960596195, "start": 23.248963910694968, "label": "2023 \u2022 JACKET \u2022 inner", "is_positive": false}, {"year": 2023, "category": "TSHIRT", "impact": -0.16246975189864427, "kind": "inner", "end": 22.95742220869755, "start": 23.119891960596195, "label": "2023 \u2022 TSHIRT \u2022 inner", "is_positive": false}, {"year": 2023, "category": "PANTS", "impact": -0.21876005026772086, "kind": "inner", "end": 22.738662158429833, "start": 22.95742220869755, "label": "2023 \u2022 PANTS \u2022 inner", "is_positive": false}], "data-f28063f888fbd67e94d16ee44839474a": [{"label": [2023], "total": 22.738662158429833}]}}, {"mode": "vega-lite"});
</script>



This is better than reporting the average footprint and unit produced separately. It's more informative to quantify their contribution to the change in emissions. Here it's good to confirm that the decrease in emissions is mostly due to a reduction in the number of units produced for both years. But it's also good to see that there was an increase due to the average footprint in 2023. Importantly, each one of these effects is calculated, and not just assumed.

It's natural to want to deepen the analysis. For instance:

1. Why is there a significant inner contribution for pants in 2022? Is it because the materials are less sustainable? Or because the pants got heavier?
2. The reduction in 2023 is mainly due to the reduction in the number of units produced. Can this be broken down into marketing segments? For instance, is the reduction mainly driven by online or in-person sales? How does this break down by country?

These questions hint at the interactive aspect of this kind of analysis. Once you break down a metric's evolution along a dimension, the next steps are to break down the metric (question 1) and/or include another dimension (question 2).

</br>
