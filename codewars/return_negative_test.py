from nose.tools import assert_equal as assertEqual
from return_negative import make_negative

def test_make_negative_large_negative():
    assertEqual(make_negative(42),-42)
def test_make_negative_small_negative():
    assertEqual(make_negative(-9),-9)
def test_make_negative_zero():
    assertEqual(make_negative(0),0)
