"""
test_contracts.py
Wilberto Morales
wilbertomorales777@gmail.com

This was my first project developed using somewhat TDD(thanks to @nwinklareth).

"""

import unittest
from contracts import require, RequirementBreached, ContractParamsError
from helpers import flip
from conditions import is_int, is_string, is_float, is_num, \
    not_zero, are_ints


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


class TestRequire(unittest.TestCase):
    """
    Tests for a contract's requirement.
    """

    def test_require_return(self):
        @require(is_string)
        def greet(name):
            return "hello %s" % name

        h = greet("Wil")
        self.assertEquals(h, "hello Wil")

        self.assertRaises(RequirementBreached, greet, 1)

    def test_require_ints(self):
        @require(are_ints)
        def asum(ns):
            return sum(ns)

        # should return the value of 'asum' if requirements met
        self.assertEquals(asum([1, 2, 3, 4, 5]), 15)
        # or raise an error if not met
        self.assertRaises(RequirementBreached, asum, ['A', 'B', 'C'])

    def test_require_many_params(self):
        @require(is_int, is_int)
        def raise_to(n, power):
            return n ** power

        # should be able to decorate a function
        # with multiple params
        self.assertEquals(raise_to(3, 3), 27)

    def test_nullable_param(self):
        @require(None, is_int)
        def times(o, n):
            return o * n

        self.assertEquals(times('a', 3), 'aaa')
        self.assertEquals(times(3, 3), 9)
        self.assertRaises(RequirementBreached, times, 'a', 0.1)

    def test_multiple_requirements(self):
        @require(is_num, is_num)
        @require(None, not_zero)
        def divide(n, by):
            return n / by

        self.assertEquals(divide(4, 4), 1)
        self.assertRaises(RequirementBreached, divide, 4, 0)
        self.assertRaises(RequirementBreached, divide, '3', 3)

    def test_with_too_many_args(self):
        # TODO: decorating should trow the error instead of calling the function
        @require(is_string, is_int, is_num, is_float)
        def hello(name):
            return "Hello sneaky %s" % (name)

        self.assertRaises(ContractParamsError, hello, 'Wil')

    def test_with_too_little_params(self):

        @require()
        def hello(name):
            return "Hello other sneaky %s" % (name)

        self.assertRaises(ContractParamsError, hello, 'Wil')

