# Neighbourhoods

## Introduction

[Representation](representation.md) allows us to determine whether a category is over-, under- or
normally represented in the different areal units. We simply define
neighbourhoods as the areal units where the different categories are
over-represented.

## Measures

----

### **overrepresented_units** (distribution, classes=*None*)

This functions outputs, for each category, a list of areal units where this
category is overrepresented.


**Parameters**

* `distribution`  dictionary
> Takes a dictionary of dictionaries with  
> distribution[areal_unit][category] = number 
* `classes` dictionary, optional
> Takes a dictionary of lists with classes[class] = [cat1, cat2, ...]  
> If not specified, the algorithm will use the categories found in
> `distribution`

**Output**

* `units` dictionary
> Returns a dictionary of lists with  
> units[category] = [unit1, ..., unitN]

----

### **neighbourhoods** (distribution, areal_units, classes=*None*)

This function takes the distribution of income and the areal units' shape (as a
[Shapely Polygon object](http://toblerity.org/shapely/manual.html) and outputs the clusters where the different categories
are overrepresented, or neighbourhoods. 

Two areal units are said to belong to the same cluster if they are contiguous,
i.e. if the intersection of their respective perimeter is a line.

**Parameters**

* `distribution`  dictionary
> Takes a dictionary of dictionaries with  
> distribution[unit_id][category] = number 
* `areal_units` dictionary
> Takes a dictionary of [Shapely Polygon objects](http://toblerity.org/shapely/manual.html) with   
> areal_units[unit_id] = areal_unit_polygon_object
* `classes` dictionary, optional
> Takes a dictionary of lists with classes[class] = [cat1, cat2, ...]  
> If not specified, the algorithm will use the categories found in
> `distribution`

**Output**

* `neighbourhoods` dictionary
> Returns a dictionary of lists of lists with  
> neighbourhoods[category] = [[unit in cluster1], ..., [units in cluster N]]

## Examples

Let us look in the following example at how to extract the neighbourhoods from
the distribution of individuals from different categories using Marble, and plot
a map of the city showing the units where category 1 is overrepresented using
matplotlib.

We assume that the distribution is contained in the variable `city`. The shape
of the areal units are contained in a shapefile located at
`path/to/areal_units.shp`.

```python
import fiona
from shapely.geometry import shape

units = {}
with fiona.open('path/to/areal_units.shp', 'r', 'ESRI Shapefile') as source:
    for f in source:
       units[f['properties']['ID_FIELD']] = shape(f['geometry'])
```

This imports the areal units as [Shapely Polygon Objects](http://toblerity.org/shapely/manual.html) and store them in the variable `units`.

```python
import marble as mb

overrepresented = mb.overrepresented_units(city)
```

This finds the areal units where the different categories are overrepresented.

```python
from maptlotlib import pylab as plt
from descartes import PolygonPatch

fig = plt.figure()
ax = fig.add_subplot(111)

for au in units:
    color = 'white'
    if au in overrepresented[1]:
        color = 'black' # Plot in black the units where 0 is overrepresented
    if units[au].geom_type=="Polygon":
        patch = PolygonPatch(units[au], fc=color, ec='None', alpha=1, zorder=1)
        ax.add_patch(patch)
    else:
        for t in units[au]:
            patch = PolygonPatch(t, fc=color, ec='None', alpha=1, zorder=1)
            ax.add_patch(patch)

ax.relim()
ax.axis('off')
ax.autoscale_view(True,True,True)
plt.show()
```
This plots the areal units where individuals belonging to category 1 are
overrepresented in black, and the others in white.
