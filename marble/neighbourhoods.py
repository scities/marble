# -*- coding: utf-8 -*-
"""neighbourhoods.py

Scripts to extract the areal units where the different classes are
over-represented, and cluster the areal units that have common boundaries.
"""
import math
import marble as mb


__all__ = ["overrepresented_units",
           "neighbourhoods"]


#
# Helper functions
#


#
# Callable functions
#
def overrepresented_units(distribution, classes=None):
    """ Find the areal units in which each class is over-represented
   
    We say that a class `\alpha` is overrepresented in that tract `t` if the
    representation `r_\alpha(t)` is such that

    .. math::
        r_\alpha(t) > 1 + 2.57 \sigma_\alpha(t)

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

    areal_units: dictionary of lists
        Dictionnary of classes, with the list of areal units where this class is
        overrepresented with 99% confidence.
        > {class:[list of areal units]}
    """

    ## Compute the representation of the different classes in all areal units
    rep = mb.representation(distibution, classes)

    ## Find the tracts where classes are overrepresented
    areal_units = {cl:[b for b in rep[cl]
                        if rep[cl][b][0] > 1 + 2.57*math.sqrt(rep[cl][b][1])] 
                    for cl in rep}

    return area_units


def neighbourhoods(distribution, areal_units, classes=None):
    """ Return the neighbourhoods where different classes gather

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

    neighbourhoods: dictionary
        Dictionary of classes names with list of neighbourhoods (that are
        each represented by a list of areal unit)
        > {'class': [ [areal units in cluster i], ...]}
    """
    neighbourhoods = {}

    ## Find the areal units where classes are overrepresented
    or_units = overrepresented_units(distribution, classes)

    return neighbourhoods
