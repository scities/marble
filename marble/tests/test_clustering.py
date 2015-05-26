""" Tests for the clustering computation """
from nose.tools import *
import itertools
from shapely.geometry import Polygon
import marble as mb


#
# Synthetic data for tests
#
def grid():
    """ Areal units arranged in a grid """
    au = [i*3+j for i,j  in itertools.product(range(3), repeat=2)]
    units = {a:Polygon([(a%3, a/3),
                        (a%3, 1+a/3),
                        (1+a%3, 1+a/3),
                        (1+a%3, a/3)]) for a in au}
    return units

def checkerboard_city():
    city = {0: {"A":100, "B":1},
            1: {"A":1, "B":100},
            2: {"A":100, "B":1},
            3: {"A":1, "B":100},
            4: {"A":100, "B":1},
            5: {"A":1, "B":100},
            6: {"A":100, "B":1},
            7: {"A":1, "B":100},
            8: {"A":100, "B":1}}
    return city

def clustered_city():
    city = {0: {"A":100, "B":1},
            1: {"A":100, "B":1},
            2: {"A":1, "B":100},
            3: {"A":100, "B":1},
            4: {"A":1, "B":100},
            5: {"A":1, "B":100},
            6: {"A":100, "B":1},
            7: {"A":1, "B":100},
            8: {"A":1, "B":100}}
    return city



#
# Perform tests
#
class TestClustering(object):

    def test_clustering_checkerboard(self):
        units = grid()
        city = checkerboard_city() 
        c = mb.clustering(city, units)

        assert c["A"] == 0.0
        assert c["B"] == 0.0

    def test_clustering_checkerboard(self):
        units = grid()
        city = clustered_city() 
        c = mb.clustering(city, units)

        assert c["A"] == 1.0
        assert c["B"] == 1.0

