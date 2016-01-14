#!/usr/bin/env python3

# --------------------
# FunctionUnpacking.py
# --------------------

import collections

print("FunctionUnpacking.py")

def f (x, y, z) :
    return [x, y, z]

t = (3, 4)
assert t            == (3, 4)
assert t            != (4, 3)
assert f(2, t, 5)   == [2, (3, 4), 5]
assert f(2, 5, t)   == [2, 5, (3, 4)]
assert f(2, *t)     == [2, 3, 4]
assert f(z = 2, *t) == [3, 4, 2]
assert f(*t, z = 2) == [3, 4, 2]

d1 = {"z" : 4, "y" : 3, "x" : 2}
assert f(**d1) == [2, 3, 4]

d2 = {"z" : 4, "y" : 3}
assert f(2,     **d2) == [2, 3, 4]
assert f(x = 2, **d2) == [2, 3, 4]

d3 = {"y" : 3}
assert f(2, z = 4, **d3) == [2, 3, 4]

t  = (2, 3)
d4 = {"z" : 4}
assert f(*t, **d4) == [2, 3, 4]

print("Done.")
