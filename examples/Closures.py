#!/usr/bin/env python3

# -----------
# Closures.py
# -----------

print("Closures.py")

def add_closure_1 (i) :
    return lambda j : i + j

i = 2
f = add_closure_1(i)
assert f(3) == 5
assert i    == 2

def add_closure_2 (x) :
    return lambda j : x[0] + j

x = [2]
f = add_closure_2(x)
x = [3]
assert f(3) == 5
assert x    == [3]

x = [2]
f = add_closure_2(x)
x[0] = 3
assert f(3) == 6
assert x    == [3]

def add_closure_3 (x) :
    def g (j) :
        x[0] += 1
        return x[0] + j
    return g

x = [2]
f = add_closure_3(x)
assert f(3) == 6
assert x    == [3]

class A :
    def __init__ (self) :
        self.a = []

    def get (self) :
        return self.a

    def add (self, v) :
        self.a.append(v)

x = A()
assert x.get() == []
x.add(2)
assert x.get() == [2]
x.add(3)
assert x.get() == [2, 3]
x.a += [4]                   # violation of interface
assert x.get() == [2, 3, 4]
x.a = None                   # violation of interface
assert x.get() == None
assert "a"     in x.__dict__
del x.a                      # violation of interface
assert "a" not in x.__dict__

def A () :
    a = []

    class B :
        def get (self) :
            return a

        def add (self, v) :
            a.append(v)

    return B()

x = A()
assert x.get() == []
x.add(2)
assert x.get() == [2]
x.add(3)
assert x.get() == [2, 3]
#x.a += [4]                  # AttributeError: 'A' object has no attribute 'a'
assert x.get() == [2, 3]
#del x.a                     # AttributeError: a
assert "a" not in x.__dict__
x.a = None                   # ?
assert "a"     in x.__dict__
assert x.get() == [2, 3]

print("Done.")
