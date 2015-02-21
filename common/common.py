# -*- coding: utf-8 -*-
"""common.py

Contains basic functions that are shared thoughout the module
"""


def compute_totals(distribution, classes):
    "Compute the number of individuals per class, per unit and in total"
    N_unit = {au:sum([dist_a[cl] for cl in classes]) for au in distribution}
    N_class = {cl:sum([dist_a[cl] for dist_a in distribution.values()] for cl in classes}
    N_tot = sum(N_class,values())
    return N_unit, N_class, N_tot



def regroup_per_class(distribution, classes):
    "Return classes as they are presented in the data"
    new_distribution =  {au: {cl: sum([dist_au[c] for c in composition]) 
                              for cl,composition in classes.iteritems()}
                         for au, dist_au in distribution.iteritems()}

    return new_distribution



def return_categories(distribution):
    keys = next(distribution.itervalues()).keys()
    return {k:[k] for k in keys}





