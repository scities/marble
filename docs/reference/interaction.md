# Interaction

## Introduction

Having found a way to quantify the [presence](representation.md) of
categories in the various areal units, and identified
[neighbourhoods](neighbourhoods.md), we would like to quantify the extent to
which individuals form various categories are exposed to one another, the extent
to which they interact with one another.

## Measure

----

### **exposure** (distribution, classes=*None*)

The following measure of exposure is inspired by a measure proposed by Marcon &
Puech to study the co-localisation of firms. In our case, it reads

$$E_{\alpha \beta} = \frac{1}{N} \sum_{t=1}^T n(t)\, r_\alpha(t)\, r_\beta(t)$$

Although it is not straightforward when written in this form,  the exposure
is the average representation of $\beta$ witnessed by the $\alpha$, or
conversely the average representation of \alpha witnessed by the $\beta$. It is
independent of the city's overall inequality levels.

In the unsegregated configuration, the exposure is equal on average to

$$\mathrm{E} \left [E_{\alpha \beta} \right] = 1$$

In other words, the diferent categories are indifferent to one another. The
variance of the exposure in the unsegregated configuration,  $\mathrm{Var}(E_{\alpha \beta})$, can also be computed
analytically.

**Parameters**

* `distribution`  dictionary
> Takes a dictionary of dictionaries with  
> distribution[areal_unit][category] = number 
* `classes` dictionary, optional
> Takes a dictionary of lists with classes[class] = [cat1, cat2, ...]  
> If not specified, the algorithm will use the categories found in
> `distribution`

**Output**

* `exposure` 
> Returns a dictionary of dictionaries with  
exposure[alpha][beta] = ($\mathrm{E}_{\alpha \beta}$, $\mathrm{Var}(E_{\alpha \beta})$)

----

## Examples

Let us look at how to compute the exposure for the categories 0, 1 and 2 in a
fictional region with two areal units A and B.

```python
>>> import marble as mb
>>> city = {"A":{0: 10, 1:0, 2:23},
          "B":{0: 0, 1:10, 2:8}}
>>> exp = mb.exposure(city)
>>> exp[0][1] # Value of the exposure between cat. 0 and 1
(0, 0.01)
```

Now, imagine that for some reason, you have found that the original categories
in fact split in two classes: first, that is composed of the category 0, and
second, that is composed of categories 1 and 2.

```python
>>> import marble as mb
>>> city = {"A":{0: 10, 1:0, 2:23},
          "B":{0: 0, 1:10, 2:8}}
>>> classes = {'first': [0], 
             'second': [1,2]}
>>> exp = mb.exposure(city, classes)
>>> exp['first']['second']
(0.867, 0.002)
```
