""" Tests for the representation computation """
import math
from nose.tools import *
import marble as mb



#
# Synthetic data for tests
#
def uniform_city():
    """ Uniform repartition """
    city = {"A":{1:1, 2:10, 3:7},
            "B":{1:2, 2:20, 3:14},
            "C":{1:4, 2:40, 3:28}}
    return city


def fake_city():
    """ Fake repartition (Random Generator) """
    # ["A"][1] not random on purpose
    city = {"A":{1:0, 2:17, 3:7},
            "B":{1:11, 2:1, 3:8},
            "C":{1:9, 2:16, 3:2}}
    return city


def missing_class_city():
    """ When an entire category is not present """
    city = {"A":{1:0, 2:10, 3:0},
            "B":{1:2, 2:20, 3:0},
            "C":{1:4, 2:40, 3:0}}
    return city


def empty_unit_city():
    """ When an entire unit is empty """
    city = {"A":{1:0, 2:0, 3:0},
            "B":{1:2, 2:20, 3:14},
            "C":{1:4, 2:40, 3:28}}
    return city


#
# Tests
#
class TestRepresentation(object):
    
    def test_uniform_repartition(self):
        """ When the population is uniformly distributed """
        city = uniform_city()
        r = mb.representation(city)
        r_answer = {"A":{1:1.0, 2:1.0, 3:1.0},
                    "B":{1:1.0, 2:1.0, 3:1.0},
                    "C":{1:1.0, 2:1.0, 3:1.0}}
        for au in r:
            for cat in r[au]: 
                assert_almost_equal(r[au][cat][0],
                                    r_answer[au][cat])
        

    def test_no_one(self):
        """ When a unit is empty of a given category """
        city = fake_city()
        r = mb.representation(city)
        assert_almost_equal(r["A"][1][0], 0)


    def test_missing_class(self):
        """ When the zone is empty of a given category """
        city = missing_class_city()
        r = mb.representation(city)
        for au in r:
            assert_true( math.isnan(r[au][3][0]) )


    def test_empty_unit(self):
        """ When an areal unit is empty """
        city = empty_unit_city()
        r = mb.representation(city)
        for cat in r["A"]:
            assert_true( math.isnan(r["A"][cat][0]) )


    def test_fake_city(self):
        """ Test on values computed by hand """
        city = fake_city()
        r = mb.representation(city)

        # Answers
        r_answer = {"A":{1:0, 2:1.479, 3:1.218},
                    "B":{1:1.9525, 2:0.104, 3:1.6705},
                    "C":{1:1.183, 2:1.237, 3:0.309}}

        var_answer = {"A":{1:0.0979, 2:0.0575, 3:0.1151},
                      "B":{1:0.1275, 2:0.0750, 3:0.1500},
                      "C":{1:0.0814, 2:0.0479, 3:0.0958}}

        # Test
        for au in r:
            for cat in r[au]: 
                assert_almost_equal(r[au][cat][0],
                                    r_answer[au][cat],
                                    places=3)
                assert_almost_equal(r[au][cat][1],
                                    var_answer[au][cat],
                                    places=3)
