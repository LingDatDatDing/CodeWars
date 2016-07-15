from nose.tools import assert_equal as assertEqual
import return_negative

def test_make_negative_large_negative():
    assertEqual(return_negative.make_negative(42),-42)
def test_make_negative_small_negative():
    assertEqual(return_negative.make_negative(-9),-9)
def test_make_negative_zero():
    assertEqual(return_negative.make_negative(0),0)
