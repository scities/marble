# -*- coding: utf-8 -*-
"""representation.py

Compute the representation of the different populations in the areal units
provided as an input.

See [Louf:2015]_ for the definition of the different quantities
"""
from __future__ import division

import marble as mb
from common import (regroup_per_class,
                   return_categories,
                   compute_totals)


__all__ = ['representation']



#
# Helper functions
#
def single_representation(n, n_unit, N_class, N_tot):
    "Compute the representation of a population in a given areal unit"
    if N_class != 0 and n_unit != 0:
        return (n/n_unit) / (N_class/N_tot)
    else:
        return float('nan') 


def single_variance(n_unit, N_class, N_tot):
    "Compute the standard deviation in a given areal unit"
    if N_class != 0 and n_unit != 0:
        return (1/N_class)*((N_tot/n_unit) - 1)
    else:
        return float('nan')




#
# Callable functions
#
def representation(distribution, classes=None):
    """ Compute the representation of the different classes in all areal units

    Parameters
    ----------

    distribution: nested dictionaries
        Number of people per class, per areal unit as given in the raw data
        (ungrouped). The dictionary must have the following formatting:
        > {areal_id: {class_id: number}}

    classes: dictionary of lists
        When the original categories need to be aggregated into different
        classes. 
        > {class: [categories belonging to this class]}
        This can be arbitrarily imposed, or computed with uncover_classes
        function of this package.

    Returns
    -------

    representation: nested dictionnaries
        Representation of each category in each areal unit.
        > {areal_id: {class_id: (representation_values, variance of the null
                                model)}}
    """
    # Regroup into classes if specified. Otherwise return categories indicated
    # in the data
    if classes:
        distribution = regroup_per_class(distribution, classes)
    else:
       classes = return_categories(distribution) 


    # Compute the total numbers per class and per individual
    N_unit, N_class, N_tot = compute_totals(distribution, classes) 


    # Compute the representation and standard deviation for all areal units
    representation = {au:{cl:(single_representation(dist_au[cl],
                                                    N_unit[au],
                                                    N_class[cl],
                                                    N_tot), 
                              single_variance(N_unit[au],
                                               N_class[cl],
                                               N_tot) 
                             ) for cl in classes}
                      for au, dist_au in distribution.iteritems()}
    
    return representation
