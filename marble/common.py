# -*- coding: utf-8 -*-
"""common.py

Contains basic functions that are shared throughout the module
"""



__author__ = """\t""".join(["Rémi Louf <remi.louf@sciti.es>"])



def compute_totals(distribution, classes):
    "Compute the number of individuals per class, per unit and in total"
    N_unit = {au:sum([distribution[au][cl] for cl in classes]) for au in distribution}
    N_class = {cl:sum([dist_a[cl] for dist_a in distribution.values()]) for cl in classes}
    N_tot = sum(N_class.values())
    return N_unit, N_class, N_tot



def regroup_per_class(distribution, classes):
    "Return classes as they are presented in the data"
    
    ## Elementary tests
    cat_input = [cat for values in classes.values() for cat in values]
    cat = return_categories(distribution).keys()

    # If repetition in the classes
    if len(set(cat_input)) != len(cat_input):
        raise ValueError("A category is present in different classes. "
                         "Check your `classes` dictionary.")

    # If a category is missing in classes
    if len(set(cat)) > len(set(cat_input)):
        raise ValueError("A category is missing in the definition of classes. "
                         "Check your `classes` dictionary.")

    # If there are more categories specified than in the data
    if len(set(cat)) < len(set(cat_input)):
        raise ValueError("There are more categories in the definition of classes "
                         "than in the data. Check your `classes` dictionary.")


    ## Regroup
    try:
        new_distribution =  {au: {cl: sum([dist_au[c] for c in composition]) 
                                  for cl,composition in classes.iteritems()}
                             for au, dist_au in distribution.iteritems()}

    except KeyError:
        raise KeyError("Verify that the categories specified in the class"
                       " definitions exist in the original data.")


    return new_distribution



def return_categories(distribution):
    "Return the categories in the original data"
    keys = next(distribution.itervalues()).keys()
    return {k:[k] for k in keys}





