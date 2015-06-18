""" Tests for the exposure computation """
from __future__ import division
from nose.tools import *
import itertools
import marble as mb



#
# Synthetic data for tests
#
def segregated_city():
    """ perfect segregation """
    city = {"A":{1:7, 2:0, 3:0},
            "B":{1:0, 2:0, 3:14},
            "C":{1:0, 2:42, 3:0}}
    return city

def two_way_city():
    """ perfect two-way exposure for 1 and 2 """
    city = {"A":{1:20, 2:28, 3:0},
            "B":{1:10, 2:14, 3:0},
            "C":{1:0, 2:0, 3:37}}
    return city

def uniform_city():
    """ Uniform representation """
    city = {"A":{1:1, 2:10, 3:7},
            "B":{1:2, 2:20, 3:14},
            "C":{1:4, 2:40, 3:28}}
    return city



#
# Test
#
class TestExposure(object):

    def test_maximum_isolation(city):
        city = segregated_city()
        exp = mb.exposure(city)
        N_cl = {i: sum([city[au][i] for au in city]) for i in [1,2,3]}
        N_tot = sum(N_cl.values())
        for c in exp:
            assert_almost_equal(exp[c][c][0], 
                                N_tot/N_cl[c], 
                                places=3)
                                
    def test_minimum_exposure(city):
        city = segregated_city()
        exp = mb.exposure(city)
        for c0,c1 in itertools.permutations([1,2,3], 2):
            assert_almost_equal(exp[c0][c1][0],
                                0.0)

    def test_maximum_exposure(city):
        city = two_way_city()
        exp = mb.exposure(city)
        N_cl = {i: sum([city[au][i] for au in city]) for i in [1,2,3]}
        N_tot = sum(N_cl.values())
        assert_almost_equal(exp[2][1][0],
                            N_tot/(N_cl[1]+N_cl[2]),
                            places=3)

    def test_minimum_isolation(city):
        city = uniform_city()
        exp = mb.exposure(city)
        for c in [1,2,3]:
            assert_almost_equal(exp[c][c][0],
                                1.0,
                                places=3)

