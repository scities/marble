""" Tests for the common computations """
from nose.tools import *
import marble as mb
import os,sys
foo_dir = os.path.dirname(os.path.join(os.getcwd(), __file__))
sys.path.append(os.path.normpath(os.path.join(foo_dir, '..')))
from common import (return_categories,
                    compute_totals,
                    regroup_per_class)


#
# Functions to generate synthetic data
#
def fake_city():
    dist = {"A": {1:0, 3:13, 4:3, 5:56, 6:9, 7:42, 8:8},
        "B": {1:0, 3:9, 4:34, 5:10, 6:0, 7:34, 8:8}}
    return dist


#
# The tests
#
class TestCommonCalculations(object):


    def test_return_categories(self):
        """ Return categories """
        city = fake_city()
        cat = return_categories(city)
        cat_answer = {1:[1], 3:[3], 4:[4], 5:[5], 6:[6], 7:[7], 8:[8]}
        assert_equal(cat, cat_answer)


    def test_compute_totals(self):
        """ Compute totals """
        city = fake_city()
        cat = return_categories(city)
        N_au, N_class, N_tot = compute_totals(city, cat)
        
        # Answers computed by hand
        Ntot_answer = 226
        Nclass_answer = {1:0, 3:22, 4:37, 5:66, 6:9, 7:76, 8:16}
        Nau_answer = {"A":131, "B":95}

        # Test
        assert N_tot == Ntot_answer
        assert_equal(N_class, Nclass_answer)
        assert_equal(N_au, Nau_answer)


    def test_same_class(self):
        """ Use original categories as classes """
        city = fake_city()
        cat = return_categories(city)
        dist = regroup_per_class(city, cat)
        assert_equal(city, dist)


    def test_missing_category(self):
        """ When a category is missing in the provided class definition """
        city = fake_city()
        cat = {"A":[1], "B":[3,4,7], "C":[5,8]}
        assert_raises(ValueError, regroup_per_class, city, cat)


    def test_too_many_category(self):
        """ When too many categories are given in the class definition"""
        city = fake_city()
        cat = {"A":[1], "B":[3,4,6,7], "C":[5,8,10]}
        assert_raises(ValueError, regroup_per_class, city, cat)


    def test_non_existent_category(self):
        """ When a non-existing category is specified in the class definition"""
        city = fake_city()
        cat = {"A":[1], "B":[3,6,7], "C":[5,8,10]}
        assert_raises(KeyError, regroup_per_class, city, cat)
