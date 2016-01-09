#!/usr/bin/env python3

# -------------
# Exceptions.py
# -------------

# https://docs.python.org/3.2/library/exceptions.html

def f (b) :
    if b :
        raise NameError("abc")
    return 0

print("Exceptions.py")

try :
    assert f(False) == 0
except NameError :
    assert False

try :
    assert f(True) == 1
    assert False
except NameError as e :
    assert type(e)      is     NameError
    assert type(e.args) is     tuple
    assert len(e.args)  ==     1
    assert e.args       is not ("abc",)
    assert e.args       ==     ("abc",)
else :
    assert False

assert type(NameError) is type
assert type(type)      is type

assert issubclass(NameError,     Exception)
assert issubclass(Exception,     BaseException)
assert issubclass(NameError,     BaseException)
assert issubclass(BaseException, object)

print("Done.")
