"""
test_contracts.py
Wilberto Morales
wilbertomorales777@gmail.com

This was my first project developed using TDD thanks to @nwinklareth.

"""

import unittest
from contracts import require, RequirementBreached

def is_string(s):
    return isinstance(s, str)

def is_int(n):
    return isinstance(n, int)

def list_of_ints(l):
    for x in l:
        if not is_int(x):
            return False
    return True

# list of functions to test with decorator
@require(is_string)
def greet(name):
    return "hello %s" % (name)

@require(list_of_ints)
def asum(ns):
    return sum(ns)

class TestRequire(unittest.TestCase):

    def test_require_return(self):
        h = greet("Wil")
        self.assertEquals(h, "hello Wil")

    def test_require_int(self):
        self.assertRaises(RequirementBreached, asum, ['A', 'B', 'C'])

