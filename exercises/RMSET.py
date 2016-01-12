#!/usr/bin/env python3

# --------
# RMSET.py
# --------

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.sqrt.html
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.square.html
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.subtract.html

from timeit   import timeit
from unittest import main, TestCase

from RMSE import            \
    rmse_while,             \
    rmse_range_for,         \
    rmse_zip_for,           \
    rmse_zip_reduce,        \
    rmse_map_sum,           \
    rmse_zip_list_sum,      \
    rmse_zip_generator_sum, \
    rmse_numpy

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            rmse_while,
            rmse_range_for,
            rmse_zip_for,
            rmse_zip_reduce,
            rmse_map_sum,
            rmse_zip_list_sum,
            rmse_zip_generator_sum,
            rmse_numpy]

    def test_0 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f((2, 3, 4), (2, 3, 4)), 0)

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f((2, 3, 4), (3, 2, 5)), 1)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f((2, 3, 4), (4, 1, 6)), 2)

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f((2, 3, 4), (4, 3, 2)), 1.632993161855452)

    def test_r (self) :
        for f in self.a :
            with self.subTest() :
                print()
                print(f.__name__)
                t = timeit(f.__name__ + "(10000 * [1], 10000 * [5]) == 4", "from __main__ import " + f.__name__, number = 100)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" :
    main()

"""
% RMSET
....
rmse_while
555.48 milliseconds

rmse_range_for
405.71 milliseconds

rmse_zip_for
372.29 milliseconds

rmse_zip_reduce
479.23 milliseconds

rmse_map_sum
489.49 milliseconds

rmse_zip_list_sum
347.59 milliseconds

rmse_zip_generator_sum
364.65 milliseconds

rmse_numpy
119.36 milliseconds
.
----------------------------------------------------------------------
Ran 5 tests in 3.140s

OK
"""
