# Presence in areal units

## Introduction

Maybe the most fundamental quantity in all studies of segregation is how we
quantify the presence of a category in areal units. All other measures are then
based on the measure of presence. Several indicators exist, and one needs to be
aware of their meaning, their qualities and their shortcomings. Per se, if one's
goal is to indentify areal units with high levels of segregation *everything
else being equal*, one should use the representation defined below. Other
measures can have their use, but are biaised and thus cannot be used for an
assessment of segregation.

## Measures

----

### **concentration** (distribution, classes=*None*)

The concentration measures the proportion of individuals from category $\alpha$
in the areal unit $t$. 

$$\frac{n_\alpha(t)}{N_\alpha}$$

The concentration has the nice property to be composition-invariant, that is it
does not depend on the relative proportion of category $\alpha$ in the
geographical zone as a whole. 

However, it strongly depends on the total population of the areal unit we are
studying: more population areal units will mechanically lead to higher values of
the concentration. Segregation measures based on the concentration (such as the
dissimilarity index) will thefore be dominated by the values in highly
population areal units.

**Parameters**

* `distribution`  dictionary
> Takes a dictionary of dictionaries with distribution[areal_unit][category] =
> number 
* `classes` dictionary, optional
> Takes a dictionary of lists with classes[class] = [cat1, cat2, ...]  
> If not specified, the algorithm will use the categories found in
> `distribution`

**Output**

* `concentration` dictionary
> Returns a dictionary of dictionaries with  
> concentration[areal_unit][category] = value

----

### **proportion** (distribution, classes=*None*)

Sometimes, however, we prefer to know the proportion of people of a given
category in an unit. In our notations, it is defined as 

$$\frac{n_\alpha(t)}{n(t)}$$

Although the values of the proportion are easier to interpret (`x% of the
individuals living in this areal units live in this neighbourhood'), they are
not a good indicator of segregation. They strongly depend on the relative
proportion of individuals of the category in the geographical area being
studied. 

**Parameters**

* `distribution`  dictionary
> Takes a dictionary of dictionaries with distribution[areal_unit][category] =
> number 
* `classes` dictionary, optional
> Takes a dictionary of lists with classes[class] = [cat1, cat2, ...]  
> If not specified, the algorithm will use the categories found in
> `distribution`

**Output**

* `proportion` dictionary
> Returns a dictionary of dictionaries with  
> proportion[areal_unit][category] = value

--------

### **representation** (distribution, classes=*None*)

The representation solves the problems linked to both measures of concentration
and of representation. The idea behind the measure of representation is that
segregation is a departure from the situation where all categories would be
spatially distributed at random. The properties of such a `random', unsegregated
city are however well known, and the distribution of categories in each areal
unit is given by a binomial distribution. The representation is thus defined as
the number $n_\alpha(t)$ divided by its expected value in an unsegregated city

$$r_\alpha(t) \frac{n_\alpha(t) / n(t)}{N_\alpha / N} $$

In the perfectly unsegregated city (number of individuals equal to the mean of
the binomial distribution), $r_\alpha = 1$. Of course, there always is a
possibility for any situation that it has been obtained by chance. Given the
binomial distribution, however, we can compute how likely it is that the
representation $r_\alpha(t)$ we measure has been obtained by chance. To do that,
we first compute the variance:

$$\mathrm{Var}\left[r_\alpha(t)\right] = \sigma_\alpha(t)^2 = \frac{1}{N_\alpha} \left[\frac{N}{n(t)} - 1\right]$$

we would like to know the areal units that depart form the random situation with
99% confidence. Therefore, we will say that  

* $\alpha$ is overrepresented in $t$ iff $r_\alpha(t) > 1 +
  2.57*\sigma_\alpha(t)
* $\alpha$ is underrepresented in $t$ iff $r_\alpha(t) < 1 +
  2.57*\sigma_\alpha(t)

!!! Beware
    The knowledge of both $r_\alpha(t)$ and
    $\mathrm{Var}\left[r_\alpha(t)\right]$ is necessary to speak of
    *underrepresentation* or *overrepresentation*.

**Parameters**

* `distribution`  dictionary
> Takes a dictionary of dictionaries with distribution[areal_unit][category] =
> number 
* `classes` dictionary, optional
> Takes a dictionary of lists with classes[class] = [cat1, cat2, ...]  
> If not specified, the algorithm will use the categories found in
> `distribution`


**Output**

* `representation` dictionary
> Returns a dictionary of dictionaries with
> representation[areal_unit][category] = ($r_\alpha(t)$,
> $\mathrm{Var}\left[r_\alpha(t)\right]$)


## Examples
