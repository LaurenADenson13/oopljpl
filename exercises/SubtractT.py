#!/usr/bin/env python3

# ------------
# SubtractT.py
# ------------

# https://docs.python.org/3/library/functions.html#subtract

from numpy    import subtract
from timeit   import timeit
from unittest import main, TestCase

from Subtract import    \
    subtract_range_for, \
    subtract_for,       \
    subtract_while,     \
    subtract_comprehension

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            subtract_range_for,
            subtract_for,
            subtract_while,
            subtract_comprehension,
            subtract]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                x = f([2, 3, 4], [2, 3, 4])
                self.assertEqual(list(x), [0, 0, 0])
                self.assertEqual(list(x), [0, 0, 0])

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                x = f([2, 3, 4], [1, 2, 3])
                self.assertEqual(list(x), [1, 1, 1])
                self.assertEqual(list(x), [1, 1, 1])

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                x = f([2, 3, 4], [1, 4, 3])
                self.assertEqual(list(x), [1, -1, 1])
                self.assertEqual(list(x), [1, -1, 1])

if __name__ == "__main__" :
    main()
