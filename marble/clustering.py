# -*- coding: utf-8 -*-
"""clustering.py

Investigate the clustering properties of neighbourhoods.
"""
from __future__ import division
import math
import shapely
import networkx as nx

import marble as mb
from common import (regroup_per_class,
                   return_categories,
                   compute_totals)



__author__ = """\t""".join(["Rémi Louf <remi.louf@sciti.es>"])

__all__ = ["clustering"]



#
# Helper functions
#
def _single_clustering(Nu, Nc):
    """Compute clustering index
    
    Parameters
    ----------
    Nu: int
        Number of units
    Nc: int
        Number of clusters
        
    Returns
    -------
    clust: float
        0 if units are not clustered (checkerboard)
        1 if units form a single cluster
    """
    clust = 1 - ( ((Nc/Nu) - (1/Nu)) /
                  (1 - (1/Nu)) ) 

    return clust




#
# Callable functions
#
def clustering(distribution, areal_units, classes=None):
    """ Return the clustering coefficient for the different classes
    
    Assume that the class `c` is overrepresented in `N_u` areal units, and that
    we obtain `N_c` clusters after aggregating the neighbourhings units.
    Parameter
    ---------

    distribution: nested dictionaries
        Number of people per class, per areal unit as given in the raw data
        (ungrouped). The dictionary must have the following formatting:
        > {areal_id: {class_id: number}}

    areal_units: dictionnary
        Dictionnary of areal unit ids with shapely polygon object representing
        the unit's geometry as values.

    classes: dictionary of lists
        When the original categories need to be aggregated into different
        classes. 
        > {class: [categories belonging to this class]}
        This can be arbitrarily imposed, or computed with uncover_classes
        function of this package.

    Returns
    -------

    clustering: dictionary
        Dictionary of classes names with clustering values.
    """

    # Regroup into classes if specified. Otherwise return categories indicated
    # in the data
    if not classes:
       classes = return_categories(distribution) 
    
    ## Get the number of neighbourhoods
    neigh = mb.neighbourhoods(distribution, areal_units, classes)
    num_neigh = {cl: len(neigh[cl]) for cl in classes}
    num_units = {cl: len([a for ne in neigh[cl] for a in ne])
                    for cl in classes}

    ## Compute clustering values
    clustering = {}
    for cl in classes:
        if num_units[cl] == 0:
            clustering[cl] = float('nan')
        elif num_units[cl] == 1:
            clustering[cl] = 1
        else:
            clustering[cl] = _single_clustering(num_units[cl],
                                                num_neigh[cl])

            clustering[cl] = ((num_neigh[cl] - num_units[cl]) /
                              (1 - num_units[cl]))
    return clustering
