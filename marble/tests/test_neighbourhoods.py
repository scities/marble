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
    au = [i*3+j for i,j  in itertools.product(range(3), repeat=2)]
    units = {a:Polygon([(a%3, a/3),
                        (a%3, 1+a/3),
                        (1+a%3, 1+a/3),
                        (1+a%3, a/3)]) for a in au}
    return units



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

# Test that for a grid, corners are not neighbours (.touch might have to go)
# Test clustering on a situation

