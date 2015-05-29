# Marble

Study residential segregation, with Python.

<div id="check"></div>

### Features

* Many measures implemented (see below for a peek)
* Inherits the simplicity of the python language
* Open source ([BSD license](about/license.md))
* Leverage other python libraries for spatial analysis, statistics, and to plot
  maps.


### Measures implemented

* [`representation`](reference/representation.md) - Compute the representation of categories in areal units.
* [`exposure`](reference/interaction.md) - Compute the exposure and isolation of categories.
* [`uncover_classes`](reference/classes.md) - Regroup categories in classes based on their spatial
  pattern of interactions.
* [`neighbourhoods`](reference/neighbourhoods.md) - Find the neighbourhoods where categories cluster.
* [`clustering`](reference/neighbourhoods.md) -  Compute the clustering index of categories.
* [`dissmilarity`](reference/evenness.md) - Compute the (traditional) dissimilarity index.


## Install

### Pypi (stable version)

You can install Marble via the Pypi repository. In a linux environment, type

```bash
sudo pip install marble
```

This should install Marble and its dependencies. You can now import Marble by
typing

```python
import marble as mb
```

at the begining of your programs (or in the python interpreter).

### Github (development)


