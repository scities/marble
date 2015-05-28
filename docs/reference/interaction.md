## Interaction


### exposure *(distribution, classes=None)*

$$E_{\alpha \beta} = \frac{1}{N} \sum_{t=1}^T n(t)\, r_\alpha(t)\, r_\beta(t)$$

Although it is not straightforward when written in this form,  the exposure
is the average representation of \beta witnessed by the \alpha, or
conversely the average representation of \alpha witnessed by the \beta. It is
independent of the city's overall inequality levels.

In the unsegregated city, the exposure is equal on average to

$$\mathrm{E} \left [E_{\alpha \beta} \right] = 1$$

In other words, the diferent categories are indifferent to one another. The
variance of the exposure is given, in the unsegregated city, by

$$\mathrm{Var} \left[E_{\alpha \beta}\right] = $$

**Parameters**

* `distribution`  dictionary
> {areal unit: {category: number of individuals}}
* `classes` dictionary, optional
> {class: [categories]}  
> If not classes are specified, the algorithm will use the categories found in
> `distribution`

**Output**

* `exposure` 
> Returns a dictionary of dictionaries with  
exposure[alpha][beta] = (E_{\alpha \beta}, Var(E_{\alpha \beta})

**Example**

Let us look at how to compute the exposure for the categories 0, 1 and 2 in a
fictional region with two areal units A and B.

```python
>>> import marble as mb
>>> city = {"A":{0: 10, 1:0, 2:23},
          "B":{0: 0, 1:10, 2:8}}
>>> mb.exposure(city)
{0: {0: , 1:, 2:},
 1: {0: , 1:, 2:},
 2: {0: , 1:, 2:}}
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
>>> mb.exposure(city, classes)
{'first':{'first':, 'second': },
'second': {'first':, 'second':}}
```

### exposure *(distribution, classes=None)*

$$E_{\alpha \beta} = \frac{1}{N} \sum_{t=1}^T n(t)\, r_\alpha(t)\, r_\beta(t)$$

Although it is not straightforward when written in this form,  the exposure
is the average representation of \beta witnessed by the \alpha, or
conversely the average representation of \alpha witnessed by the \beta. It is
independent of the city's overall inequality levels.

In the unsegregated city, the exposure is equal on average to

$$\mathrm{E} \left [E_{\alpha \beta} \right] = 1$$

In other words, the diferent categories are indifferent to one another. The
variance of the exposure is given, in the unsegregated city, by

$$\mathrm{Var} \left[E_{\alpha \beta}\right] = $$

**Parameters**

* `distribution`  dictionary
> {areal unit: {category: number of individuals}}
* `classes` dictionary, optional
> {class: [categories]}  
> If not classes are specified, the algorithm will use the categories found in
> `distribution`

**Output**

* `exposure` 
> Returns a dictionary of dictionaries with  
exposure[alpha][beta] = (E_{\alpha \beta}, Var(E_{\alpha \beta})

**Example**

Let us look at how to compute the exposure for the categories 0, 1 and 2 in a
fictional region with two areal units A and B.

```python
>>> import marble as mb
>>> city = {"A":{0: 10, 1:0, 2:23},
          "B":{0: 0, 1:10, 2:8}}
>>> mb.exposure(city)
{0: {0: , 1:, 2:},
 1: {0: , 1:, 2:},
 2: {0: , 1:, 2:}}
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
>>> mb.exposure(city, classes)
{'first':{'first':, 'second': },
'second': {'first':, 'second':}}
```

