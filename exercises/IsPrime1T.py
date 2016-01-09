#!/usr/bin/env python3

# ------------
# IsPrime1T.py
# ------------

# https://en.wikipedia.org/wiki/Primality_test

from math     import sqrt
from unittest import main, TestCase

from IsPrime1 import is_prime

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertFalse(is_prime(1))

    def test_2 (self) :
        self.assertFalse(is_prime(2))

    def test_3 (self) :
        self.assertTrue(is_prime(3))

    def test_4 (self) :
        self.assertFalse(is_prime(4))

    def test_5 (self) :
        self.assertTrue(is_prime(5))

    def test_7 (self) :
        self.assertTrue(is_prime(7))

    def test_9 (self) :
        self.assertTrue(is_prime(9))

    def test_27 (self) :
        self.assertFalse(is_prime(27))

    def test_29 (self) :
        self.assertTrue(is_prime(29))

if __name__ == "__main__" :
    main()

"""
% IsPrime1T.py
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
"""
