#!/usr/bin/env python3

# ------------------
# FileInputOutput.py
# ------------------

import sys
import types

assert type(sys)   is types.ModuleType
assert type(types) is types.ModuleType

assert type(sys.argv) is list
assert len(sys.argv)  == 1

assert sys.argv is not ["./FileInputOutput.py"]
assert sys.argv ==     ["./FileInputOutput.py"]

f = open(sys.argv[0])

for v in f :
    print(v, end = "")
