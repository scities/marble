# -*- coding: utf-8 -*-
"""classes.py

Functions to uncover the classes that emerge from the spatial repartition of the
original categories.
"""
import csv
from common import compute_totals

__all__ = ['cluster_categories',
            'uncover_classes']



#
# Helper functions
#
def _aggregate_linkage(categories, linkage):
    " Aggregate until the M value is < than 1 "
    agg = categories
    print agg
    print linkage
    for l in linkage[len(categories):]:
        print l
        if l[2]>1:
           agg.append("%s|%s"%(agg[l[0]],agg[l[1]]))
           agg[l[0]] = 0
           agg[l[1]] = 0
    return [a for a in agg if a!=0]


def _find_friends(E, N_class):
    """ Find the two categories with highest M value and return
    Be careful to normalise properly the M-values above 1!  
    """

    ## Normalise the values above one by the maximum
    E_norm = E.copy()
    for c0 in E_norm:
        for c1, e in E_norm[c0].iteritems():
            if e>1:
                max_e = sum(N_class.values())*(N_class[c0]+N_class[c1]) \
                         / 4*N_class[c0]*N_class[c1]
                E_norm[c0][c1] = 1 + (e-1)/(max_e-1) 


    ## Discard isolation values
    E_norm_nodiag = {c0:{c1:(E[c0][c1] 
                                if c1!=c0 else 0) 
                          for c1 in E[c0]}
                     for c0 in E}


    ## Find the pair of categories with the highest mutual attraction
    (alpha, beta) = max( [(c0, c1, val) for c0, subdict in E_norm_nodiag.iteritems() 
                          for c1, val in subdict.iteritems()], 
                          key=lambda x:x[2])[:2]

    return alpha, beta




def _update_matrix(M_new, M_std_new, H_class, a, b):
    ## New index
    l = max(H_class.keys())+1

    ## Compute new M-values
    # Compute new lines
    new = {cl:(1/(H_class[a]+H_class[b]))*(H_class[a]*M_new[a][cl] + H_class[b]*M_new[b][cl]) for cl in M_new if cl not in [a,b]}
    diag = (1/(H_class[a]+H_class[b]))*(H_class[a]*M_new[a][a] +
            H_class[b]*M_new[b][b])
    # Delete the old categories 
    for cl0 in M_new:
       M_new[cl0].pop(a, None)
       M_new[cl0].pop(b, None)
    M_new.pop(a, None)
    M_new.pop(b, None)
    # Add new lines
    for cl0 in M_new:
        M_new[cl0][l] = new[cl0]
    M_new[l] = new
    M_new[l][l]=diag
   

    ## Compute new standard deviations
    # New lines
    new = {cl:(1/(H_class[a]+H_class[b]))*
              math.sqrt(((H_class[a]**2)*(M_std_new[a][cl]**2) +
                         (H_class[b]**2)*(M_std_new[b][cl]**2)))
           for cl in M_std_new if cl not in [a,b]}
    diag = (1/(H_class[a]+H_class[b]))* math.sqrt(((H_class[a]**2)*(M_std_new[a][a]**2) +
                         (H_class[b]**2)*(M_std_new[b][b]**2)))
    for cl0 in M_std_new:
       M_std_new[cl0].pop(a, None)
       M_std_new[cl0].pop(b, None)

    M_std_new.pop(a, None)
    M_std_new.pop(b, None)
    # Add new lines
    for cl0 in M_std_new:
        M_std_new[cl0][l] = new[cl0]
    M_std_new[l] = new
    M_std_new[l][l] = diag 

    ## update H_class
    H_class[l] = H_class[a] + H_class[b]
    H_class.pop(a, None)
    H_class.pop(b, None)

    return (M_new, M_std_new, H_class)




#
# Callable functions
#
def cluster_categories(distribution, exposure, classes=None):
    """ Perform hierarhical clustering on the intra-tract exposure values 
    
    At each step of the aggregation, we look for the pair `(\beta, \delta)` of
    categories that has the highest exposure (renormalised by the maximum
    possible value). We aggregate them in a new category `\gamma` whose exposure
    with the other categories `\alpha` is given by

    .. math::
        E_{\alpha, \gamma} = \frac{1}{N_\beta + N_\delta} \left( N_\beta
        E_{\alpha, \beta} + N_\delta M_{\alpha, \delta} \right)

    We only aggregate the pair if the two categories attract each other, that is
    if the exposure
   
   .. math::
        E_{\beta, \delta} > 1 + 10 \sigma_{\beta, \delta} 
        
    (99 CI according to the Chebyshed inequality). The aggregation procedure
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

    linkage: list of tuples
        list L that encodes the hierarhical tree. At the ith iteration of the
        algorithm, L[i,0] and L[i,1] are aggregated to form the n+ith cluster. The
        exposure between L[i,1] and L[i,0] is given by L[i,3].
    """
    #
    # Data preparation
    #

    ## Linkage matrix
    linkage = [cl for cl in sorted(exposure, key=lambda x: int(x))]
    N = len(linkage)

    ## Get totals
    N_unit, N_class, N_tot = compute_totals(distribution, classes) 

    

    ## Use classes' position in the linkage matrix rather than names

    # Class totals
    for cl in classes:
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
        a, b = find_friends(E, N_class)
        linkage.append((a, b, E[a][b], E_var[a][b])) 
        E, E_var, N_class = update_matrix(E, E, N_class, a, b) 


    return linkage 



def uncover_classes(linkage, ci_factor=10):
    """ Returns the categories sorted in classes

    The classes are uncovered using the spatial repartition of individuals from
    different categories, using their relative exposure.

    Parameters
    ----------

    linkage: list of tuples
        list L that encodes the hierarhical tree. At the ith iteration of the
        algorithm, L[i,0] and L[i,1] are aggregated to form the n+ith cluster. The
        exposure between L[i,1] and L[i,0] is given by L[i,3].

    Returns
    -------

    classes: dictionary
        Dictionnary of classes with the list of the corresponding original
        categories as values.
        > {'class':[categories]}
    """

