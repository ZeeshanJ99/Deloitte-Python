from test_unittest_calculator import SciCalculator


c = SciCalculator()

def test_find_sqrt():
    assert c.find_sqrt(100) == 10
    assert c.find_sqrt(None) is None

def test_find_ceil():
    assert c.find_ceil(12.7) == 13
    assert c.find_ceil(3.14) == 4


# import math
# square root and ceil