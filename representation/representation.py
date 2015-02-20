# -*- coding: utf-8 -*-
"""representation.py

Compute the representation of the different populations in the areal units
provided as an input.

See [Louf:2015]_ for the definition of the different quantities
"""

__all__ = ['representation']


#
# Helper functions
#
def compute_totals(distribution, classes):
    "Compute the number of individuals per class, per unit and in total"
    N_unit = {au:sum([dist_a[cl] for cl in classes]) for au in distribution}
    N_class = {cl:sum([dist_a[cl] for dist_a in distribution.values()] for cl in classes}
    N_tot = sum(N_class,values())
    return N_unit, N_class, N_tot

def single_representation()

#
# Callable functions
#
def representation(distribution, classes=None):
    representation = 
  
    # Compute the total numbers per class and per individual
    N_unit, N_class, N_tot = compute_totals(distribution) 

    for areal_unit in distribution:
        rep = single_representation(distribution[areal_unit][cl], 
