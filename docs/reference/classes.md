# Emergent classes

Using the [representation](representation.md) as a measure of interaction
between classes, we can aggregate the different categories into classes based on
their mutual interaction/repulsion.

## Measures

----

### **cluster_categories** (distribution, exposure)

At each step of the aggregation, we look for the pair $(\beta, \delta)$ of
categories that has the highest exposure (renormalised by the maximum
possible value). We aggregate them in a new category $\gamma$ whose exposure
with the other categories $\alpha$ is given by

$$ E_{\alpha, \gamma} = \frac{1}{N_\beta + N_\delta} \left( N_\beta\,
E_{\alpha, \beta} + N_\delta\, E_{\alpha, \delta} \right)
$$

The function return a linkage matrix that encode the hierarchical tree. At the $i$th iteration of the
algorithm, $L[i,0]$ and $L[i,1]$ are aggregated to form the $n+i$th cluster. The
exposure between $L[i,1]$ and $L[i,0]$ is given by $L[i,3]$, the variance in the
corresponding unsegregated city is given by $L[i,4]$.

**Parameters**

* `distribution`  dictionary
> Takes a dictionary of dictionaries with  
> distribution[areal_unit][category] = number 
* `exposure` dictionary
> Takes a dictionary dictionary of dictionaries, the result of the
> [exposure](interaction.md) function with  
> exposure[$\alpha$][$\beta$] = ($E_{\alpha \beta}$, $\mathrm{Var}(E_{\alpha \beta})$)

**Output**

* `linkage matrix` 
> Returns a list of lists. See above for the description of the linkage matrix's
> structure.

----

### **uncover_classes** (distribution, exposure, ci_factor=*10*)

The classes are uncovered using the spatial repartition of individuals from
different categories, using their relative exposure.

We only aggregate the pair $\beta$,$\delta$  in the same class if the two categories attract each other, that is
if the exposure

$$E_{\beta, \delta} > 1 + 10 \sigma_{\beta, \delta}$$
    
($99\%$ CI according to the Chebyshev inequality). The aggregation procedure
may therefore stop before all categories are aggregated in one unique class,
and output the classes repartition of the original categories. 

**Parameters**

* `distribution`  dictionary
> Takes a dictionary of dictionaries with  
> distribution[areal_unit][category] = number 
* `exposure` dictionary
> Takes a dictionary dictionary of dictionaries, the result of the
> [exposure](interaction.md) function with  
> exposure[$\alpha$][$\beta$] = ($E_{\alpha \beta}$, $\mathrm{Var}(E_{\alpha \beta})$)
* `ci_factor` float
> Number of standard deviations over which we consider to have a $99\%$
> confidence interval on the exposure value. The default value $10$, is the
> upper bound given by Chebyshev's inequality.

**Output**

* `classes` nested lists
> Returns a list of lists. Each list corresponds to a class with  
> classes[$i$] = [categories in class $i$] 
