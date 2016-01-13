#!/usr/bin/env python3

# -----------
# Subtract.py
# -----------

def subtract_range_for (a, p) :
    l = []
    for i in range(len(a)) :
        l.append(a[i] - p[i])
    return l

def subtract_for (a, p) :
    l = []
    z = zip(a, p)
    for x, y in z :
        l.append(x - y)
    return l

def subtract_while (a, p) :
    l = []
    x = iter(a)
    y = iter(p)
    try :
        while True :
            l.append(next(x) - next(y))
    except StopIteration :
        pass
    return l

def subtract_comprehension (a, p) :
    z = zip(a, p)
    return [x - y for x, y in z]
