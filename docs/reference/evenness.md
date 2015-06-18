# (un)Evenness

### **dissimilarity** (distribution, classes=*None*)

The index, popularised by Duncan & Duncan in 1955, measures the different in
concentration between the different categories.

The dissimilarity between the categories $\alpha$ and $\beta$ is defined as

$$D_{\alpha \beta} = \frac{1}{2} \sum_{t=1}^T \left| \frac{n_\alpha(t)}{N_\alpha} - \frac{n_\beta(t)}{N_\beta} \right|$$

By construction, we have $D \in \left[0, 1\right]$, with $D=1$ when the
categories are never present in the same areal units (perfect segregation) and
$D=0$ when their respective concentrations are identical in all units.

**Parameters**

* `distribution`  dictionary
> Takes a dictionary of dictionaries with  
> distribution[areal_unit][category] = number 
* `classes` dictionary, optional
> Takes a dictionary of lists with classes[class] = [cat1, cat2, ...]  
> If not specified, the algorithm will use the categories found in
> `distribution`

**Output**

* `dissimilarity` 
> Returns a dictionary of dictionaries with  
dissimilarity[alpha][beta] = $D_{\alpha \beta}$ 

