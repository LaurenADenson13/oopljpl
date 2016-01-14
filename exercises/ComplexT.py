#!/usr/bin/env python3

# ----------
# Complex.py
# ----------

# https://docs.python.org/3/library/stdtypes.html#typesnumeric

from unittest import main, TestCase

from Complex import my_complex

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            my_complex,
               complex]

    def test_1 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c()
                self.assertEqual(x.real, 0)
                self.assertEqual(x.imag, 0)

    def test_2 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c(2)
                self.assertEqual(x.real, 2)
                self.assertEqual(x.imag, 0)

    def test_3 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c(2, 3)
                self.assertEqual(x.real, 2)
                self.assertEqual(x.imag, 3)

    def test_4 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c(2, 3)
                s = str(x)
                self.assertEqual(s, "(2+3j)") # x.__str__()

    def test_5 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c(2, 3)
                y = c(2, 3)
                self.assertEqual(x, y)        # x.__eq__(y)

    def test_6 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c(2, 3)
                y = c(4, 5)
                x = x + y                     # x = x.__add__(y)
                self.assertEqual(x, c(6, 8))

    def test_7 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c(2, 3)
                y = c(4, 5)
                x += y                        # x = x.__add__(y)
                self.assertEqual(x, c(6, 8))

    def test_8 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c(4, 5)
                y = c(2, 3)
                x = x - y                     # x = x.__sub__(y)
                self.assertEqual(x, c(2, 2))

    def test_9 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c(4, 5)
                y = c(2, 3)
                x -= y                        # x = x.__isub__(y)
                self.assertEqual(x, c(2, 2))

    def test_10 (self) :
        for c in self.a :
            with self.subTest(c = c) :
                x = c(2, 3)
                y = x.conjugate()             # y = A.conjugate(x)
                self.assertEqual(x, c(2,  3))
                self.assertEqual(y, c(2, -3))

if __name__ == "__main__" :
    main()
