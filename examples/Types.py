#!/usr/bin/env python3

# --------
# Types.py
# --------

import sys
from types import FunctionType

print("Types.py")

b = True
b = False
assert type(b)    is bool
assert type(bool) is type
assert issubclass(bool, bool)
assert issubclass(bool, object)

i = 2
assert type(i)   is int
assert type(int) is type
assert issubclass(int, int)
assert issubclass(int, object)

assert issubclass(bool, int)

f = 2.3
assert type(f)     is float
assert type(float) is type
assert issubclass(float, float)
assert issubclass(float, object)

c = 2 + 3j
assert type(c)       is complex
assert type(complex) is type
assert issubclass(complex, complex)
assert issubclass(complex, object)

s = 'abc'
s = "abc"
assert type(s)   is str
assert type(str) is type
assert issubclass(str, str)
assert issubclass(str, object)

l = [2, "abc", 3.45]
assert type(l)    is list
assert type(list) is type
assert issubclass(list, list)
assert issubclass(list, object)

t = (2, "abc", 3.45)
assert type(t)     is tuple
assert type(tuple) is type
assert issubclass(tuple, tuple)
assert issubclass(tuple, object)

s = {2, "abc", 3.45}
assert type(s)   is set
assert type(set) is type
assert issubclass(set, set)
assert issubclass(set, object)

d = {2 : "def", 3.45 : 3, "abc" : 6.78}
assert type(d)    is dict
assert type(dict) is type
assert issubclass(dict, dict)
assert issubclass(dict, object)

def f (v) :
    return v + 1
assert type(f)            is FunctionType
assert type(FunctionType) is type
assert issubclass(FunctionType, FunctionType)
assert issubclass(FunctionType, object)

class A :
    def __init__ (self, i, f) :
        self.i = i
        self.f = f

x = A(2, 3.45)
assert type(x) is A
assert type(A) is type
assert issubclass(A, A)
assert issubclass(A, object)

assert type(type) is type
assert issubclass(type, type)
assert issubclass(type, object)

print("Done.")
