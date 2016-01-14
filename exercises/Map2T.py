#!/usr/bin/env python3

# --------
# Map2T.py
# --------

# https://docs.python.org/3/library/functions.html#map

from unittest import main, TestCase

class MyUnitTests (TestCase) :
    def test_1 (self) :
        a = ()
        self.assertEqual(list(map(lambda x : x ** 2, a)), [])

    def test_2 (self) :
        a = (2, 3, 4)
        self.assertEqual(list(map(lambda x : x ** 2, a)), [4, 9, 16])

    def test_3 (self) :
        a = (2, 3, 4)
        b = (5, 6, 7)
        self.assertEqual(list(map(lambda x, y : x + y, a, b)), [7, 9, 11])

    def test_4 (self) :
        a = (2, 3)
        b = (4, 5)
        c = (6, 7)
        self.assertEqual(list(map(lambda x, y, z : x + y + z, a, b, c)), [12, 15])

if __name__ == "__main__" :
    main()
