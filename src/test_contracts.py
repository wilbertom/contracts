"""
test_contracts.py
Wilberto Morales
wilbertomorales777@gmail.com

This was my first project developed using TDD thanks to @nwinklareth.

"""

import unittest
from contracts import require, RequirementBreached
from helpers import flip
from conditions import is_int, is_string, is_float, is_num, is_list_of_ints

# list of functions to test with decorator
@require(is_string)
def greet(name):
    return "hello %s" % (name)

@require(is_list_of_ints)
def asum(ns):
    return sum(ns)


class TestHelpers(unittest.TestCase):
    """
    Not all in the helpers is tested, because
    of time. However anything new from now on
    must be tested.
    """


    def test_flip(self):
        def divide(x, y):
            return x / y
        self.assertEquals(divide(100, 10), flip(divide)(10, 100))

class TestConditions(unittest.TestCase):
    """
    All conditions must be tested since the user
    might use them and other tests depend on them.
    """

    def test_is_string(self):
        self.assertTrue(is_string('Hello'))
        self.assertTrue(is_string('A'))

        self.assertFalse(is_string(1))
        self.assertFalse(is_string(0.0))


    def test_is_int(self):
        self.assertTrue(is_int(1))
        self.assertTrue(is_int(-1))
        self.assertTrue(is_int(0))

        self.assertFalse(is_int('1'))
        self.assertFalse(is_int('-1'))
        self.assertFalse(is_int('0'))
        self.assertFalse(is_int("A"))

        self.assertFalse(is_int(0.1))
        self.assertFalse(is_int(0.0))
        self.assertFalse(is_int(-0.1))


    def test_is_float(self):
        self.assertFalse(is_float(1))
        self.assertFalse(is_float(-1))
        self.assertFalse(is_float(0))

        self.assertFalse(is_float('0.0'))
        self.assertFalse(is_float('A'))

        self.assertTrue(is_float(0.0))
        self.assertTrue(is_float(1.0))
        self.assertTrue(is_float(-1.0))


    def test_is_number(self):
        self.assertTrue(is_num(0))
        self.assertTrue(is_num(1))
        self.assertTrue(is_num(-1))

        self.assertTrue(is_num(0.0))
        self.assertTrue(is_num(-1.0))
        self.assertTrue(is_num(1.0))

        self.assertFalse(is_num('0'))
        self.assertFalse(is_num('A'))


    def test_is_list_of_ints(self):
        self.assertTrue(is_list_of_ints([1, 2, 3, 4, 5]))
        self.assertTrue(is_list_of_ints([1]))

        self.assertFalse(is_list_of_ints([]))
        self.assertFalse(is_list_of_ints([1.0, 2, 3, 4, 5]))
        self.assertFalse(is_list_of_ints([1, 2, 'A', 4, 5]))



class TestRequire(unittest.TestCase):
    """
    Tests for a contract's requirement

    """


    def test_require_return(self):
        h = greet("Wil")
        self.assertEquals(h, "hello Wil")


    def test_require_int(self):
        # should return the value of asum if requirements met
        self.assertEquals(asum([1, 2, 3, 4, 5]), 15)
        # or raise an error if not met
        self.assertRaises(RequirementBreached, asum, ['A', 'B', 'C'])


