
# Plotly Express: Conceptual Mindmap for Markmap

## Plotly Express: Mental Model

- **Two Layers of Plotly**
  - `plotly.graph_objects`: Low-level API for full control and custom dashboards.
  - `plotly.express`: High-level API for quick, single-line exploratory plots.
    - *Note*: Plotly Express always returns a `plotly.graph_objects.Figure` object.

---

## Core Structure

- **Figure Object Structure**
  - `data`: Plot traces (scatter, bar, etc.)
  - `layout`: Styling (title, legend, margins)
  - `frames`: Animation support (optional)

---

## Visualization Types (Function Categories)

- **Scatter-Based Charts** (Relationships, Correlations)
  - `px.scatter`: 2D scatter plot
  - `px.scatter_3d`: 3D scatter plot
  - `px.scatter_polar`: Polar coordinates
  - `px.scatter_ternary`: Ternary plots (3-component ratios)
  - `px.scatter_geo`: Geographical scatter on flat maps
  - `px.scatter_mapbox`: Geo scatter on interactive Mapbox

- **Line Charts** (Trends, Time Series)
  - `px.line`: 2D line plot
  - `px.line_3d`: 3D path
  - `px.line_polar`: Polar line
  - `px.line_ternary`: Ternary line
  - `px.line_geo`, `px.line_map`, `px.line_mapbox`: Lines over geographic spaces

- **Distribution Charts** (Univariate/Grouped)
  - `px.histogram`: Frequency distribution
  - `px.box`: Quartiles, outliers
  - `px.violin`: Distribution + density
  - `px.strip`: Jittered points
  - `px.ecdf`: Empirical CDF

- **Categorical/Comparison Charts**
  - `px.bar`: Category comparison
  - `px.bar_polar`: Bar on polar axis
  - `px.timeline`: Gantt-style timelines

- **Composition (Part-to-Whole)**
  - `px.pie`: Proportions (few categories)
  - `px.treemap`: Hierarchical part-to-whole
  - `px.sunburst`: Multi-level radial proportions
  - `px.icicle`: Hierarchical rectangles
  - `px.funnel`, `px.funnel_area`: Process drop-off

- **Multivariate/Matrix Visualizations**
  - `px.scatter_matrix`: Pairwise scatter plots
  - `px.parallel_coordinates`: Numeric variable comparison
  - `px.parallel_categories`: Categorical dimension comparison

- **Geospatial Charts**
  - `px.choropleth`: Region-based coloring (non-mapbox)
  - `px.choropleth_mapbox`: Mapbox region coloring
  - `px.scatter_geo`, `px.scatter_mapbox`: Geo scatter plots

- **Density Charts**
  - `px.density_contour`: 2D KDE contours
  - `px.density_heatmap`: 2D density as colored grid
  - `px.density_mapbox`: Geo heatmap

- **Image-Based**
  - `px.imshow`: Image data, heatmaps

- **Utility Functions**
  - `set_mapbox_access_token()`: Enable Mapbox plots
  - `get_trendline_results()`: Regression output

---

## Use-Centric Chart Mapping

- **Distribution (1 variable):** `histogram`, `box`, `violin`, `ecdf`
- **Relationships (2 variables):** `scatter`, `line`, `density_contour`
- **Time Series:** `line`, `area`, `timeline`
- **Group Comparisons:** `bar`, `strip`, `box`, `violin`
- **Multivariate:** `scatter_matrix`, `parallel_coordinates`
- **Hierarchical Composition:** `treemap`, `sunburst`, `icicle`
- **Geospatial:** `choropleth_mapbox`, `scatter_geo`, `density_mapbox`
- **Dashboards:** Any chart + `update_layout()`

---

