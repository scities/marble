# Marble

Study residential segregation, with Python.

<div id="check"></div>

### Features

* Open source (BSD)

## Measures implemented

* `representation` - Compute the representation of categories in areal units.
* `exposure` - Compute the exposure and isolation of categories.
* `uncover_classes` - Regroup categories in classes based on their spatial
  pattern of interactions.
* `neighbourhoods` - Find the neighbourhoods where categories cluster.
* `clustering` -  Compute the clustering index of categories.
* `dissmilarity` - Compute the (traditional) dissimilarity index.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Another test

```python
exposure(distribution, classes=None)
```

```python
representation(distribution, classes=None)
```

```python
dissimilarity(distribution, classes=None)
```
with \[n_\alpha(t)\]

$$D_{\alpha \beta} = \frac{1}{T} \sum_{t=1}^T \left| \frac{n_\alpha(t)}{N_\alpha} - \frac{n_\beta(t)}{N_\beta} \right|$$

```python
cluster_categories(distribution, exposure)
```
Parameters

* distirbution
* categories

$$\int dx$$

```python
uncover_classes(distribution, exposure, ci_factor=10)
```
 
```python
overrepresented_units(distribution, exposure, ci_factor=10)
```

```python
neighbourhoods(distribution, exposure, ci_factor=10)
```

```python
clustering(distribution, exposure, ci_factor=10)
```
