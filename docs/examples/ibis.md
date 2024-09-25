# Different backend support with Ibis 🐦

icanexplain is implemented with [Ibis](https://github.com/ibis-project/ibis). This means that it is framework agnostic, and can work with different backends. This example shows how to use it with [DuckDB](https://duckdb.org/).


```python
import ibis
import icanexplain as ice

products_df = ice.datasets.load_product_footprints()
con = ibis.connect("duckdb://example.ddb")
con.create_table(
    "products", products_df, overwrite=True
)
```




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">DatabaseTable: example.main.products
  year       int64
  category   string
  product_id string
  footprint  float64
  units      int64
</pre>





```python
con = ibis.connect("duckdb://example.ddb")
con.list_tables()
```




    ['products']




```python
ibis.options.interactive = True
products = con.table("products")
products.head()
```




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">┏━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┓
┃<span style="font-weight: bold"> year  </span>┃<span style="font-weight: bold"> category </span>┃<span style="font-weight: bold"> product_id </span>┃<span style="font-weight: bold"> footprint </span>┃<span style="font-weight: bold"> units </span>┃
┡━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━┩
│ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">int64</span> │ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">string</span>   │ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">string</span>     │ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">float64</span>   │ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">int64</span> │
├───────┼──────────┼────────────┼───────────┼───────┤
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span> │ <span style="color: #008000; text-decoration-color: #008000">DRESS   </span> │ <span style="color: #008000; text-decoration-color: #008000">848be709  </span> │     <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">96.04</span> │   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">803</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span> │ <span style="color: #008000; text-decoration-color: #008000">DRESS   </span> │ <span style="color: #008000; text-decoration-color: #008000">658f92b3  </span> │     <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">58.15</span> │  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3367</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span> │ <span style="color: #008000; text-decoration-color: #008000">DRESS   </span> │ <span style="color: #008000; text-decoration-color: #008000">3a26f323  </span> │     <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">82.94</span> │   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">240</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span> │ <span style="color: #008000; text-decoration-color: #008000">DRESS   </span> │ <span style="color: #008000; text-decoration-color: #008000">6221dca6  </span> │     <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">85.94</span> │   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">432</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span> │ <span style="color: #008000; text-decoration-color: #008000">DRESS   </span> │ <span style="color: #008000; text-decoration-color: #008000">46864ac5  </span> │     <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">84.99</span> │   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">816</span> │
└───────┴──────────┴────────────┴───────────┴───────┘
</pre>





```python
explainer = ice.SumExplainer(
    fact='footprint',
    count='units',
    group='category',
    period='year'
)
explanation = explainer(products)
explanation
```




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">┏━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃<span style="font-weight: bold"> year  </span>┃<span style="font-weight: bold"> category </span>┃<span style="font-weight: bold"> inner         </span>┃<span style="font-weight: bold"> mix           </span>┃
┡━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">int64</span> │ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">string</span>   │ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">float64</span>       │ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">float64</span>       │
├───────┼──────────┼───────────────┼───────────────┤
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2022</span> │ <span style="color: #008000; text-decoration-color: #008000">DRESS   </span> │  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3.931932e+06</span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.881370e+07</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2022</span> │ <span style="color: #008000; text-decoration-color: #008000">JACKET  </span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.510008e+07</span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-9.238617e+07</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2022</span> │ <span style="color: #008000; text-decoration-color: #008000">PANTS   </span> │  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4.002506e+07</span> │  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5.295190e+07</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2022</span> │ <span style="color: #008000; text-decoration-color: #008000">SHIRT   </span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.484809e+06</span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-5.791456e+06</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2022</span> │ <span style="color: #008000; text-decoration-color: #008000">SWEATER </span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-2.676209e+07</span> │  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1.181504e+07</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2022</span> │ <span style="color: #008000; text-decoration-color: #008000">TSHIRT  </span> │  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6.650940e+06</span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-2.311836e+07</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2023</span> │ <span style="color: #008000; text-decoration-color: #008000">DRESS   </span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-4.078094e+06</span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.240339e+07</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2023</span> │ <span style="color: #008000; text-decoration-color: #008000">JACKET  </span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-6.793317e+06</span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-4.924036e+07</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2023</span> │ <span style="color: #008000; text-decoration-color: #008000">PANTS   </span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.636299e+07</span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-2.295608e+08</span> │
│  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2023</span> │ <span style="color: #008000; text-decoration-color: #008000">SHIRT   </span> │  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8.920908e+05</span> │ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-4.019144e+06</span> │
│     <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">…</span> │ <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">…</span>        │             <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">…</span> │             <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">…</span> │
└───────┴──────────┴───────────────┴───────────────┘
</pre>





```python
type(explanation)
```




    ibis.expr.types.relations.Table




```python
explanation.execute()
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
      <th>year</th>
      <th>category</th>
      <th>inner</th>
      <th>mix</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2022</td>
      <td>DRESS</td>
      <td>3.931932e+06</td>
      <td>-1.881370e+07</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2022</td>
      <td>JACKET</td>
      <td>-1.510008e+07</td>
      <td>-9.238617e+07</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2022</td>
      <td>PANTS</td>
      <td>4.002506e+07</td>
      <td>5.295190e+07</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2022</td>
      <td>SHIRT</td>
      <td>-1.484809e+06</td>
      <td>-5.791456e+06</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2022</td>
      <td>SWEATER</td>
      <td>-2.676209e+07</td>
      <td>1.181504e+07</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2022</td>
      <td>TSHIRT</td>
      <td>6.650940e+06</td>
      <td>-2.311836e+07</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2023</td>
      <td>DRESS</td>
      <td>-4.078094e+06</td>
      <td>-1.240339e+07</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2023</td>
      <td>JACKET</td>
      <td>-6.793317e+06</td>
      <td>-4.924036e+07</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2023</td>
      <td>PANTS</td>
      <td>-1.636299e+07</td>
      <td>-2.295608e+08</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2023</td>
      <td>SHIRT</td>
      <td>8.920908e+05</td>
      <td>-4.019144e+06</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2023</td>
      <td>SWEATER</td>
      <td>-5.701391e+06</td>
      <td>-1.130507e+08</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2023</td>
      <td>TSHIRT</td>
      <td>-1.150391e+07</td>
      <td>-8.391323e+07</td>
    </tr>
  </tbody>
</table>
</div>




```python
ibis.to_sql(explanation)
```




```sql
SELECT
  *
FROM (
  SELECT
    "t9"."year",
    "t9"."category",
    "t9"."count_lag" * (
      "t9"."mean" - "t9"."mean_lag"
    ) AS "inner",
    (
      "t9"."count" - "t9"."count_lag"
    ) * "t9"."mean" AS "mix"
  FROM (
    SELECT
      "t8"."category",
      "t8"."year",
      "t8"."mean",
      "t8"."count",
      LAG("t8"."mean", 1) OVER (PARTITION BY "t8"."category" ORDER BY "t8"."year" ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "mean_lag",
      LAG("t8"."count", 1) OVER (PARTITION BY "t8"."category" ORDER BY "t8"."year" ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "count_lag"
    FROM (
      SELECT
        "t7"."category",
        "t7"."year",
        COALESCE("t7"."mean", 0) AS "mean",
        COALESCE("t7"."count", 0) AS "count"
      FROM (
        SELECT
          "t3"."category",
          "t4"."year",
          "t6"."mean",
          "t6"."count"
        FROM (
          SELECT DISTINCT
            "t0"."category"
          FROM "products" AS "t0"
        ) AS "t3"
        CROSS JOIN (
          SELECT DISTINCT
            "t0"."year"
          FROM "products" AS "t0"
        ) AS "t4"
        LEFT OUTER JOIN (
          SELECT
            "t0"."category",
            "t0"."year",
            SUM("t0"."footprint" * "t0"."units") / SUM("t0"."units") AS "mean",
            SUM("t0"."units") AS "count"
          FROM "products" AS "t0"
          GROUP BY
            1,
            2
        ) AS "t6"
          ON "t3"."category" = "t6"."category" AND "t4"."year" = "t6"."year"
      ) AS "t7"
    ) AS "t8"
  ) AS "t9"
  ORDER BY
    "t9"."year" ASC,
    "t9"."category" ASC
) AS "t10"
WHERE
  "t10"."year" IS NOT NULL
  AND "t10"."category" IS NOT NULL
  AND "t10"."inner" IS NOT NULL
  AND "t10"."mix" IS NOT NULL
```


