# Iowa whiskey sales


```python
import icanexplain as ice

sales = ice.datasets.load_iowa_whiskey_sales()
sales.head()
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
      <th>date</th>
      <th>category</th>
      <th>vendor</th>
      <th>sales_amount</th>
      <th>price_per_bottle</th>
      <th>bottles_sold</th>
      <th>bottle_volume_ml</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012-06-04</td>
      <td>CANADIAN WHISKIES</td>
      <td>CONSTELLATION WINE COMPANY, INC.</td>
      <td>94.02</td>
      <td>15.67</td>
      <td>6</td>
      <td>1750</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-01-05</td>
      <td>STRAIGHT BOURBON WHISKIES</td>
      <td>CAMPARI(SKYY)</td>
      <td>18.76</td>
      <td>9.38</td>
      <td>2</td>
      <td>375</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-05-25</td>
      <td>CANADIAN WHISKIES</td>
      <td>DIAGEO AMERICAS</td>
      <td>11.03</td>
      <td>11.03</td>
      <td>1</td>
      <td>300</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-01-20</td>
      <td>CANADIAN WHISKIES</td>
      <td>PHILLIPS BEVERAGE COMPANY</td>
      <td>33.84</td>
      <td>11.28</td>
      <td>3</td>
      <td>750</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2012-03-19</td>
      <td>CANADIAN WHISKIES</td>
      <td>CONSTELLATION WINE COMPANY, INC.</td>
      <td>94.02</td>
      <td>15.67</td>
      <td>6</td>
      <td>1750</td>
      <td>2012</td>
    </tr>
  </tbody>
</table>
</div>




```python
import icanexplain as ice

explainer = ice.SumExplainer(
    fact='sales_amount',
    period='year',
    group='category'
)
explanation = explainer(sales)
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
      <th rowspan="8" valign="top">2016</th>
      <th>BLENDED WHISKIES</th>
      <td>17854.426840</td>
      <td>7356.773160</td>
    </tr>
    <tr>
      <th>CANADIAN WHISKIES</th>
      <td>-22278.517726</td>
      <td>225902.657726</td>
    </tr>
    <tr>
      <th>CORN WHISKIES</th>
      <td>0.000000</td>
      <td>4113.900000</td>
    </tr>
    <tr>
      <th>IRISH WHISKIES</th>
      <td>22144.484766</td>
      <td>75122.825234</td>
    </tr>
    <tr>
      <th>SCOTCH WHISKIES</th>
      <td>19591.969612</td>
      <td>-13570.609612</td>
    </tr>
    <tr>
      <th>SINGLE BARREL BOURBON WHISKIES</th>
      <td>1852.032816</td>
      <td>6375.427184</td>
    </tr>
    <tr>
      <th>STRAIGHT BOURBON WHISKIES</th>
      <td>107144.930127</td>
      <td>97934.499873</td>
    </tr>
    <tr>
      <th>STRAIGHT RYE WHISKIES</th>
      <td>-23929.320351</td>
      <td>-69208.459649</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">2020</th>
      <th>BLENDED WHISKIES</th>
      <td>83342.597187</td>
      <td>59768.582813</td>
    </tr>
    <tr>
      <th>CANADIAN WHISKIES</th>
      <td>224022.616060</td>
      <td>149363.353940</td>
    </tr>
    <tr>
      <th>CORN WHISKIES</th>
      <td>1517.480513</td>
      <td>1453.259487</td>
    </tr>
    <tr>
      <th>IRISH WHISKIES</th>
      <td>-14048.436797</td>
      <td>67344.406797</td>
    </tr>
    <tr>
      <th>SCOTCH WHISKIES</th>
      <td>19840.477504</td>
      <td>-18869.917504</td>
    </tr>
    <tr>
      <th>SINGLE BARREL BOURBON WHISKIES</th>
      <td>11958.317395</td>
      <td>3819.272605</td>
    </tr>
    <tr>
      <th>STRAIGHT BOURBON WHISKIES</th>
      <td>167864.459707</td>
      <td>268064.740293</td>
    </tr>
    <tr>
      <th>STRAIGHT RYE WHISKIES</th>
      <td>-9839.091595</td>
      <td>64056.431595</td>
    </tr>
  </tbody>
</table>
</div>




```python
explainer.plot(sales)
```





<style>
  #altair-viz-09d92760f1bc4952881e3156ea4e9c81.vega-embed {
    width: 100%;
    display: flex;
  }

  #altair-viz-09d92760f1bc4952881e3156ea4e9c81.vega-embed details,
  #altair-viz-09d92760f1bc4952881e3156ea4e9c81.vega-embed details summary {
    position: relative;
  }
</style>
<div id="altair-viz-09d92760f1bc4952881e3156ea4e9c81"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-09d92760f1bc4952881e3156ea4e9c81") {
      outputDiv = document.getElementById("altair-viz-09d92760f1bc4952881e3156ea4e9c81");
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



Funnel decomposition to break down the amount in dollars into bottles sold times by the price per bottle.
