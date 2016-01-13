#!/usr/bin/env python3

# --------------
# CommandLine.py
# --------------

"""
% CommandLine.py Nothing to be done.
"""

import sys
import types

print("CommandLine.py")

assert type(sys)   is types.ModuleType
assert type(types) is types.ModuleType

assert type(sys.argv) is list
assert len(sys.argv)  == 5

assert sys.argv is not ["./CommandLine.py", "Nothing", "to", "be", "done."]
assert sys.argv ==     ["./CommandLine.py", "Nothing", "to", "be", "done."]

print("Done.")
