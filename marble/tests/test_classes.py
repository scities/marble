""" Tests for the emergence of classes """
from nose.tools import *
import marble as mb



#
# Synthetic data for the tests
#
def uniform_city():
    """ 2-way repartition """
    city = {"A":{1:10, 2:10, 3:0},
            "B":{1:20, 2:20, 3:0},
            "C":{1:0, 2:0, 3:40}}
    return city

def segregated_city():
    """ 2-way segregation """
    city = {"A":{1:3107, 2:0, 3:0},
            "B":{1:0, 2:0, 3:1184},
            "C":{1:0, 2:1242, 3:0}}
    return city



#
# Tests
#
class TestClasses(object):

    def test_class_uniform(self):
        city = uniform_city()
        exp = mb.exposure(city)
        classes = mb.uncover_classes(city, exp)
        assert_equal(len(classes),2)

    def test_class_segregated(self):
        city = segregated_city()
        exp = mb.exposure(city)
        classes = mb.uncover_classes(city, exp)
        assert_equal(len(classes),3)
