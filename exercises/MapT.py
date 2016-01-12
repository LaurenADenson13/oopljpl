#!/usr/bin/env python3

# -------
# MapT.py
# -------

# https://docs.python.org/3.5/library/functions.html#map

from unittest import main, TestCase

from Map import    \
    map_range_for, \
    map_for,       \
    map_while,     \
    map_generator

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            map_range_for,
            map_for,
            map_while,
            map_generator,
            map]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(lambda x : x ** 2, [])
                self.assertEqual(list(x), [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(lambda x : x ** 2, [2])
                self.assertEqual(list(x), [4])
                self.assertEqual(list(x), [])

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(lambda x : x ** 3, [2, 3])
                self.assertEqual(list(x), [8, 27])
                self.assertEqual(list(x), [])

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(lambda x : x ** 2, [2, 3, 4])
                self.assertEqual(list(x), [4, 9, 16])
                self.assertEqual(list(x), [])

if __name__ == "__main__" :
    main()

"""
% MapT
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
"""
