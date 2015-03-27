# -*- coding: utf-8 -*-
"""dissimilarity.py

Compute the dissmilarity index between the different categories, as well as the
absolute dissimilarity, that we call evenness.
"""
from __future__ import division

from common import (regroup_per_class,
                   return_categories,
                   compute_totals)




__all__ = ['dissimilarity',
        'evenness']




#
# Helper functions
#
def _pair_dissimilarity(distribution, N_class, alpha, beta):
    return 0.5*sum([ abs( dist[alpha] / N_class[alpha] - 
                          dist[beta] / N_class[beta] )
                    for t,dist in distribution.iteritems()])


def _single_evenness(distribution, alpha, N_unit, N_class, N_tot):
    norm = 1 / (2* (1 - (N_class[alpha]/N_tot)))
    evenness = norm*sum([abs( dist[alpha] / N_class[alpha] -
                              N_unit[t] / N_tot) 
                        for t,dist in distribution.iteritems()])

    return evenness




#
# Callable functions
#
def dissimilarity(distribution, classes=None):
    """ Compute the inter-class dissimilarity index

    The dissimilarity index between two categories `\alpha` and `\beta` is
    defined as 

    ..math::
        D_{\alpha \beta} = \frac{1}{2} \sum_{i=1}^{T} \left|
    \frac{n_\alpha(t)}{N_\alpha} - \frac{n_\beta(t)}{N_\beta} \right|

    Its value ranges from 0 to 1.

    Parameters
    ----------

    distribution: nested dictionaries
        Number of people per class, per areal unit as given in the raw data
        (ungrouped). The dictionary must have the following formatting:
        > {areal_id: {class_id: number}}

    classes: dictionary of lists
        When the original categories need to be aggregated into different
        classes. {class: [categories belonging to this class]}
        This can be arbitrarily imposed, or computed with uncover_classes
        function of this package.

    Returns
    -------

    dissimilarity: nested dictionary
        Classes matrix with dissimilarity as values
        > {alpha: {beta: D_{\alpha \beta}}}
    """
    ## Regroup into classes if specified
    if classes is not None:
        distribution = regroup_per_class(distibution, classes)
    else:
        classes = return_categories(distibution)

    ## Compute total numbers of individuals per class and areal unit
    N_unit, N_class, N_tot = compute_totals(distribution) 

    ## Compute the dissimilarity matrix
    dissimilarity = {alpha: {beta: _pair_dissimilarity(distribution, 
                                                    N_class, 
                                                    alpha, 
                                                    beta)} 
                        for alpha, beta in itertools.combination(classes, 2)}

    return dissimilarity
