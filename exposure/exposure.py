# -*- coding: utf-8 -*-
"""exposure.py

Functions needed to compute the exposure matrix (including concentration) and
the standard deviation for the null model
"""
from __future__ import division
import itertools
import math

from ..common import (
        compute_totals, 
        regroup_per_class,
        return_categories
        )
from ..representation import representation as rep




__all__ = ["exposure"]




#
# Helper functions
#
def single_exposure(distribution, cl0, cl1):
    pass

def single_deviation(distribution, cl0, cl1):
    pass




#
# Callable functions
#
def exposure(distribution, classes):

    # Regroup into classes if specified. Otherwise return categories indicated
    # in the data
    if classes:
        distribution = regroup_per_class(distribution, classes)
    else:
       classes = return_categories(distribution) 

    # Compute the total numbers per class and per individual
    N_unit, N_class, N_tot = compute_totals(distribution) 

    # Compute representation for all areal unit
    representation = rep(distribution, classes)

    # Compute the exposure matrix
    exposure = {cl0: {cl1: (single_exposure(distribution, cl0, cl1),
                            single_deviation(distribution, cl0, cl1)) }
                for cl0, cl1 
                in itertools.combination_with_replacement(classes,2)} 

    return exposure 
