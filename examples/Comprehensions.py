#!/usr/bin/env python3

# -------------
# Indexables.py
# -------------

from types import GeneratorType

print("Comprehensions.py")

x = [2, 3, 4]
y = []
for v in x :
    y += [v * 5]
assert x == [ 2,  3,  4]
assert y == [10, 15, 20]

x = [2, 3, 4]
y = [v * 5 for v in x]            # list comprehension
assert type(y) is list
assert not hasattr(y, "__next__")
assert     hasattr(y, "__iter__")
assert x == [2,   3,  4]
assert y == [10, 15, 20]

x = [2, 3, 4]
y = (v * 5 for v in x)          # generator
assert type(y) is GeneratorType
assert hasattr(y, "__next__")
assert hasattr(y, "__iter__")
assert x       == [2,   3,  4]
assert list(y) == [10, 15, 20]
assert list(y) == []

x = [2, 3, 4]
y = map(lambda v : v * 5, x)
assert type(y) is map
assert hasattr(y, "__next__")
assert hasattr(y, "__iter__")
assert x       == [2,   3,  4]
assert list(y) == [10, 15, 20]
assert list(y) == []

x = [2, 3, 4]
y = (v * 5 for v in x)
x += [5]
assert x       == [ 2,  3,  4,  5]
assert list(y) == [10, 15, 20, 25]
assert list(y) == []
x += [5]
assert list(y) == []

x = [2, 3, 4]
y = map(lambda v : v * 5, x)
x += [5]
assert x       == [2,   3,  4,  5]
assert list(y) == [10, 15, 20, 25]
assert list(y) == []
x += [5]
assert list(y) == []

x = [2, 3, 4, 5, 6]
y = []
for v in x :
    if v % 2 :
        y += [v * 5]
assert x == [2,  3,  4,  5,  6]
assert y == [   15,     25]

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x if v % 2]
assert x == [ 2,  3,  4,  5,  6]
assert y == [    15,     25]

x = [2, 3, 4, 5, 6]
y = (v * 5 for v in x if v % 2)
assert x       == [ 2,  3,  4,  5,  6]
assert list(y) == [    15,     25]
assert list(y) == []

x = [2, 3, 4, 5, 6]
y = filter(lambda v : v % 2, x)
assert type(y) is filter
assert hasattr(y, "__next__")
assert hasattr(y, "__iter__")
z = map(lambda v : v * 5, y)
assert x       == [ 2,  3,  4,  5,  6]
assert list(z) == [    15,     25]
assert list(z) == []

x = [2, 3, 4]
y = [4, 5]
z = []
for v in x :
    for w in y :
        z += [v + w]
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]

x = [2, 3, 4]
y = [4, 5]
z = [v + w for v in x for w in y]
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]

x = [2, 3, 4]
y = [4, 5]
z = (v + w for v in x for w in y)
assert x       == [2, 3, 4]
assert y       == [4, 5]
assert list(z) == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert list(z) == []

x = {2, 3, 4}
y = set()
for v in x :
    y |= {v * 5}
assert x == { 2,  3,  4}
assert y == {10, 15, 20}

x = {2, 3, 4}
y = {v * 5 for v in x}   # set comprehension
assert x == { 2,  3,  4}
assert y == {10, 15, 20}

x = {2 : "abc", 3 : "def", 4 : "ghi"}
y = {}
for k, v in x.items() :
    y[k] = v + "xyz"
assert x == {2 : "abc",    3 : "def",    4 : "ghi"}
assert y == {2 : "abcxyz", 3 : "defxyz", 4 : "ghixyz"}

x = {2 : "abc", 3 : "def", 4 : "ghi"}
y = {k : v + "xyz" for k, v in x.items()}              # dict comprehension
assert type(y) is dict
assert not hasattr(y, "__next__")
assert     hasattr(y, "__iter__")
assert x == {2 : "abc",    3 : "def",    4 : "ghi"}
assert y == {2 : "abcxyz", 3 : "defxyz", 4 : "ghixyz"}

a = [2, 3, 4]
r = reversed(a)
assert list(r) == [4, 3, 2]
assert list(r) == []

a = ["abc", "def", "ghi"]
e = enumerate(a)
assert list(e) == [(0, "abc"), (1, "def"), (2, "ghi")]
assert list(e) == []

a = [2, 3, 4]
b = [5, 6, 7]
z = zip(a, b)
assert list(z) == [(2, 5), (3, 6), (4, 7)]
assert list(z) == []

a = [4, 2, 3]
s = sorted(a)
assert a == [4, 2, 3]
assert s == [2, 3, 4]

assert     all([True,  2, 3.45, "abc", [2, 3, 4], (2, 3, 4), {2, 3, 4}, {2 : "abc", 3 : "def", 4 : "ghi"}])
assert not any([False, 0, 0.0,  "",    [],        (),        set(),     dict()])

print("Done.")
