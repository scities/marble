# -*- coding: utf-8 -*-
"""representation.py

Compute the representation of the different populations in the areal units
provided as an input.

See [Louf:2015]_ for the definition of the different quantities
"""
from __future__ import division
import math

from ..common import (
        compute_totals, 
        regroup_per_class,
        return_categories
        )


__all__ = ['representation']


#
# Helper functions
#
def single_representation(n, n_unit, N_class, N_tot):
    "Compute the representation of a population in a given areal unit"
    return (n/n_unit) / (N_class/N_tot)


def single_deviation(n_unit, N_class, N_tot):
    "Compute the standard deviation in a given areal unit"
    return math.sqrt( (1/N_class)*((N_tot/n_unit) - 1) ) 



#
# Callable functions
#
def representation(distribution, classes=None):
   
    # Regroup into classes if specified. Otherwise return categories indicated
    # in the data
    if classes:
        distribution = regroup_per_class(distribution, classes)
    else:
       classes = return_categories(distribution) 


    # Compute the total numbers per class and per individual
    N_unit, N_class, N_tot = compute_totals(distribution) 


    # Compute the representation and standard deviation for all areal units
    representation = {au:{cl:(single_representation(dist_au[cl],
                                                    N_unit[au],
                                                    N_class[cl],
                                                    N_tot), 
                              single_deviation(N_unit[au],
                                               N_class[cl],
                                               N_tot) 
                             ) for cl in classes}
                      for au, dist_au in distribution.iteritems()}
    
    return representation
