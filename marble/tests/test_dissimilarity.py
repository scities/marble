""" Tests for the dissimilarity computation """
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

def segregated_city():
    """ perfect segregation """
    city = {"A":{1:7, 2:0, 3:0},
            "B":{1:0, 2:0, 3:14},
            "C":{1:0, 2:42, 3:0}}
    return city

def fake_city():
    """ Fake repartition (Random Generator) """
    # ["A"][1] not random on purpose
    city = {"A":{1:0, 2:17, 3:7},
            "B":{1:11, 2:1, 3:8},
            "C":{1:9, 2:16, 3:2}}
    return city


#
# Tests
#
class TestDissimilarity(object):

    def test_dissimilarity_uniform_city(self):
        """ Null values in the uniform city """
        city = uniform_city()
        d = mb.dissimilarity(city)
        d_answer = {1:{1:0, 2:0, 3:0},
                   2:{1:0, 2:0, 3:0},
                   3:{1:0, 2:0, 3:0}}
        for c0 in d:
            for c1 in d[c0]:
                assert_equal(d[c0][c1], d_answer[c0][c1])


    def test_dissimilarity_segregated_city(self):
        """ 1 in the segregated city """
        city = segregated_city()
        d = mb.dissimilarity(city)
        d_answer = {1:{1:0, 2:1, 3:1},
                   2:{1:1, 2:0, 3:1},
                   3:{1:1, 2:1, 3:0}}
        for c0 in d:
            for c1 in d[c0]:
                assert_equal(d[c0][c1], d_answer[c0][c1])


    def test_dissimilarity_fake(self):
        """ Compare dissimalirity values computed by hands """
        city = fake_city()
        d = mb.dissimilarity(city)
        d_answer = {1: {1:0.0, 2:0.5205882352941176, 3:0.411764705882353}, 
                    2: {1:0.5205882352941176, 2:0.0, 3:0.4411764705882353}, 
                    3: {1:0.411764705882353, 2:0.4411764705882353, 3:0.0}}
        for c0 in d:
            for c1 in d[c0]:
                assert_equal(d[c0][c1], d_answer[c0][c1])
