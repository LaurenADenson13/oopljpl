#!/usr/bin/env python3

# -------------
# FactorialT.py
# -------------

from math     import factorial
from timeit   import timeit
from unittest import main, TestCase

from Factorial import         \
    factorial_range_for,      \
    factorial_range_reduce,   \
    factorial_recursion,      \
    factorial_tail_recursion, \
    factorial_while

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            factorial_recursion,
            factorial_tail_recursion,
            factorial_while,
            factorial_range_for,
            factorial_range_reduce,
            factorial]

    def test_0 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(0), 1)

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(1), 1)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(2), 2)

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(3), 6)

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(4), 24)

    def test_5 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(5), 120)

    def test_6 (self) :
        for f in self.a :
            with self.subTest() :
                print()
                print(f.__name__)
                t = timeit(f.__name__ + "(100)", "from __main__ import " + f.__name__, number = 1000)
                print("{:.2f} milliseconds".format(t * 1000))
                print()

if __name__ == "__main__" :
    main()

"""
% FactorialT.py
......
factorial_recursion
21.63 milliseconds


factorial_tail_recursion
37.02 milliseconds


factorial_while
13.65 milliseconds


factorial_range_for
8.24 milliseconds


factorial_range_reduce
8.67 milliseconds


factorial
0.95 milliseconds

.
----------------------------------------------------------------------
Ran 7 tests in 0.097s

OK
"""
