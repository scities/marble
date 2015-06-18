# -*- coding: utf-8 -*-
"""classes.py

Functions to uncover the classes that emerge from the spatial repartition of the
original categories.
"""
from __future__ import division
import copy
import math
import csv

from common import (compute_totals,
                    return_categories)



__author__ = """\t""".join(["Rémi Louf <remi.louf@sciti.es>"])

__all__ = ['cluster_categories',
            'uncover_classes']



#
# Helper functions
#
def _aggregate_linkage(linkage, categories, ci_factor):
    """ Aggregate until the M value is <= than 1 
    Categories are contained in linkage... """

    agg = [[c] for c in categories]
    for l in linkage[len(categories):]:
        if l[2] > 1 + ci_factor*math.sqrt(l[3]):
           agg.append([a for a in agg[l[0]]] + [a for a in agg[l[1]]])
           agg[l[0]] = 0
           agg[l[1]] = 0

    return [a for a in agg if a!=0]


def _find_friends(E, N_class):
    """ Find the two categories with highest M value and return
    Be careful to normalise properly the M-values above 1!  
    """
    ## Normalise the values above one by the maximum
    E_norm = copy.deepcopy(E)
    for c0 in E_norm:
        for c1, e in E_norm[c0].iteritems():
            if e>1:
                max_e = sum(N_class.values()) / (N_class[c0]+N_class[c1]) 
                E_norm[c0][c1] = 1 + (e-1)/(max_e-1) 


    ## Discard isolation values
    E_norm_nodiag = {c0:{c1:(E_norm[c0][c1] 
                                if c1!=c0 else 0) 
                          for c1 in E[c0]}
                     for c0 in E}


    ## Find the pair of categories with the highest mutual attraction
    (alpha, beta) = max( [(c0, c1, val) for c0, subdict in E_norm_nodiag.iteritems() 
                          for c1, val in subdict.iteritems()], 
                          key=lambda x:x[2])[:2]

    return alpha, beta




def _update_matrix(E, E_var, N_class, a, b):
    ## New category index
    l = max(N_class.keys())+1

    #
    # Compute new exposure values 
    #

    ## Compute exposure between new category and others 
    exposure = {c: (1/(N_class[a]+N_class[b]))*(N_class[a]*E[a][c] +
                                                N_class[b]*E[b][c]) 
                for c in E if c not in [a,b]}
    isolation = (1/(N_class[a]+N_class[b])**2)*(N_class[a]**2*E[a][a] +
                                                N_class[b]**2*E[b][b] +
                                                2*N_class[a]*N_class[b]*E[a][b])

    ## Delete the old categories 
    for c0 in E:
       E[c0].pop(a, None)
       E[c0].pop(b, None)
    E.pop(a, None)
    E.pop(b, None)

    ## Add new lines to matrix
    for c0 in E:
        E[c0][l] = exposure[c0]
    E[l] = exposure
    E[l][l] = isolation
   


    #
    # Compute new exposure variance
    #
    ## Compute variance of exposure betwenn new categories and others 
    off_diag = {c:(1/(N_class[a]+N_class[b])**2)*
                   ( (N_class[a]**2)*(E_var[a][c]) +
                     (N_class[b]**2)*(E_var[b][c]))
               for c in E_var if c not in [a,b]}
    diag = (1/(N_class[a]+N_class[b])**4)*(N_class[a]**4*E_var[a][a] +
                                           N_class[b]**4*E_var[b][b] +
                                           (N_class[a]*N_class[b])**2*E_var[a][b])
    
    ## Delete the old categories
    for c0 in E_var:
       E_var[c0].pop(a, None)
       E_var[c0].pop(b, None)
    E_var.pop(a, None)
    E_var.pop(b, None)

    # Add new lines to matrix
    for c0 in E_var:
        E_var[c0][l] = off_diag[c0]
    E_var[l] = off_diag
    E_var[l][l] = diag 


    #
    # Update the number of individuals per class
    #
    N_class[l] = N_class[a] + N_class[b]
    N_class.pop(a, None)
    N_class.pop(b, None)

    return (E, E_var, N_class)




#
# Callable functions
#
def cluster_categories(distribution, exposure):
    """ Perform hierarhical clustering on the intra-tract exposure values 
    
    At each step of the aggregation, we look for the pair `(\beta, \delta)` of
    categories that has the highest exposure (renormalised by the maximum
    possible value). We aggregate them in a new category `\gamma` whose exposure
    with the other categories `\alpha` is given by

    .. math::
        E_{\alpha, \gamma} = \frac{1}{N_\beta + N_\delta} \left( N_\beta
        E_{\alpha, \beta} + N_\delta E_{\alpha, \delta} \right)


    Parameters
    ----------

    distribution: nested dictionaries
        Number of people per class, per areal unit as given in the raw data
        (ungrouped). The dictionary must have the following formatting:
        > {areal_id: {class_id: number}}

    exposure: nested dictionaries
        Matrix of exposures between categories.
        > {class_id0: {class_id1: (exposure_01, variance null model)}} 


    Returns
    -------

    linkage: list of tuples
        list L that encodes the hierarhical tree. At the ith iteration of the
        algorithm, L[i,0] and L[i,1] are aggregated to form the n+ith cluster. The
        exposure between L[i,1] and L[i,0] is given by L[i,3], the variance is
        given by L[i,4].
    """
    #
    # Data preparation
    #

    ## Linkage matrix
    linkage = [cl for cl in sorted(exposure, key=lambda x: int(x))]
    N = len(linkage)

    ## Get total
    categories = return_categories(distribution)
    N_unit, N_class, N_tot = compute_totals(distribution, categories) 

    

    ## Use classes' position in the linkage matrix rather than names
    # Class totals
    for cl in categories:
        N_class[linkage.index(cl)] = N_class.pop(cl)

    #exposure
    E = {linkage.index(cl0):{linkage.index(cl1):exposure[cl0][cl1][0]
                                for cl1 in exposure[cl0]}
            for cl0 in exposure}
    E_var = {linkage.index(cl0):{linkage.index(cl1):exposure[cl0][cl1][1]
                                for cl1 in exposure[cl0]}
            for cl0 in exposure}



    #
    # Clustering
    #
    for i in range(N-1): 
        a, b = _find_friends(E, N_class)
        linkage.append((a, b, E[a][b], E_var[a][b])) 
        E, E_var, N_class = _update_matrix(E, E_var, N_class, a, b) 


    return linkage 



def uncover_classes(distribution, exposure, ci_factor=10):
    """ Returns the categories sorted in classes

    The classes are uncovered using the spatial repartition of individuals from
    different categories, using their relative exposure.

    We only aggregate pair in the same class if the two categories attract each other, that is
    if the exposure
   
   .. math::
        E_{\beta, \delta} > 1 + 10 \sigma_{\beta, \delta} 
        
    (99% CI according to the Chebyshev inequality). The aggregation procedure
    may therefore stop before all categories are aggregated in one unique class,
    and output the classes repartition of the original categories. 

    Parameters
    ----------

    distribution: nested dictionaries
        Number of people per class, per areal unit as given in the raw data
        (ungrouped). The dictionary must have the following formatting:
        > {areal_id: {class_id: number}}

    exposure: nested dictionaries
        Matrix of exposures between categories.
        > {class_id0: {class_id1: (exposure_01, variance null model)}} 

    ci_factor: float
        Number of standard deviations over which we consider to have a 99%
        confidence interval on the exposure value. The default value, 10, is the
        upper bound given by Chebyshev's inequality.

    Returns
    -------

    classes: nested lists
        list of classes with the list of the corresponding original
        categories as values.
        > [[categories]]
    """

    ## Get the categories from the distribution
    categories = return_categories(distribution).keys()

    ## Extract the linkage matrix
    linkage = cluster_categories(distribution, exposure) 

    ## Get the classes
    classes = _aggregate_linkage(linkage, categories, ci_factor)

    return classes
