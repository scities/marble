""" Tests for the extraction of neighbourhoods """
from nose.tools import *
import itertools
from shapely.geometry import Polygon
import marble as mb
from marble.neighbourhoods import _adjacency



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
class TestNeighbourhoods(object):

    def test_adjacency(test):
        """ Test the extraction of the adjacency list """
        units = grid()
        adj = _adjacency(units)
        adj_answer = {0:[1,3],
                    1:[0,4,2],
                    2:[1,5],
                    3:[0,4,6],
                    4:[1,3,5,7],
                    5:[2,4,8],
                    6:[3,7],
                    7:[4,6,8],
                    8:[5,7]}

        for au in adj:
            assert set(adj[au]) == set(adj_answer[au])

    def test_overrepresented_check(self):
        """ Test the extraction of units with overrepresentation """
        city = checkerboard_city()
        units = mb.overrepresented_units(city)
        units_answer = {"A":[0,2,4,6,8],
                        "B":[1,3,5,7]}

        assert set(units["A"]) == set(units_answer["A"])
        assert set(units["B"]) == set(units_answer["B"])

    def test_overrepresented_clust(self):
        """ Test the extraction of units with overrepresentation """
        city = clustered_city()
        units = mb.overrepresented_units(city)
        units_answer = {"A":[0,1,3,6],
                        "B":[2,4,5,7,8]}

        assert set(units["A"]) == set(units_answer["A"])
        assert set(units["B"]) == set(units_answer["B"])

    def test_neighbourhoods_check(self):
        """ Test the extraction of neighbourhoods """
        city = checkerboard_city()
        units = grid()
        neigh = mb.neighbourhoods(city, units)
        neigh_answer = {"A":[[0],[2],[4],[6],[8]],
                        "B":[[1],[3],[5],[7]]}

        assert len(neigh["A"]) == len(neigh_answer["A"])
        assert len(neigh["B"]) == len(neigh_answer["B"])

    def test_neighbourhoods_clust(self):
        """ Test the extraction of neighbourhoods """
        city = clustered_city()
        units = grid()
        neigh = mb.neighbourhoods(city, units)
        neigh_answer = {"A":[[0,1,3,6]],
                        "B":[[2,4,5,7,8]]}

        assert len(neigh["A"]) == len(neigh_answer["A"])
        assert len(neigh["B"]) == len(neigh_answer["B"])
