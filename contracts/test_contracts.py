"""
test_contracts.py
Wilberto Morales
wilbertomorales777@gmail.com

This was my first project developed using somewhat TDD(thanks to @nwinklareth).

"""

import unittest
from contracts import require, ensure, RequirementBreached, \
    ContractParamsError, EnsuranceBreached
from conditions import is_int, is_string, is_num, \
    not_zero, are_ints, is_positive

class TestRequire(unittest.TestCase):
    """
    Tests for a contract's requirement.
    """

    def test_require_return(self):
        @require(is_string)
        def greet(name):
            return "hello %s" % name

        h = greet("Wil")
        self.assertEqual(h, "hello Wil")

        self.assertRaises(RequirementBreached, greet, 1)

    def test_require_ints(self):
        @require(are_ints)
        def asum(ns):
            return sum(ns)

        # should return the value of 'asum' if requirements met
        self.assertEqual(asum([1, 2, 3, 4, 5]), 15)
        # or raise an error if not met
        self.assertRaises(RequirementBreached, asum, ['A', 'B', 'C'])

    def test_require_many_params(self):
        @require(is_int, is_int)
        def raise_to(n, power):
            return n ** power

        # should be able to decorate a function
        # with multiple params
        self.assertEqual(raise_to(3, 3), 27)

    def test_nullable_param(self):
        @require(None, is_int)
        def times(o, n):
            return o * n

        self.assertEqual(times('a', 3), 'aaa')
        self.assertEqual(times(3, 3), 9)
        self.assertRaises(RequirementBreached, times, 'a', 0.1)

    def test_multiple_requirements(self):
        @require(is_num, is_num)
        @require(None, not_zero)
        def divide(n, by):
            return n / by

        self.assertEqual(divide(4, 4), 1)
        self.assertRaises(RequirementBreached, divide, 4, 0)
        self.assertRaises(RequirementBreached, divide, '3', 3)

    def test_with_too_many_args(self):
        # TODO: decorating should trow the error instead of calling the function
        @require(is_string, is_int, is_num)
        def hello(name):
            return "Hello sneaky %s" % (name)

        self.assertRaises(ContractParamsError, hello, 'Wil')

    def test_with_too_little_params(self):

        @require()
        def hello(name):
            return "Hello other sneaky %s" % (name)

        self.assertRaises(ContractParamsError, hello, 'Wil')


class TestEnsure(unittest.TestCase):
    def test_ensure_return(self):
        @ensure(is_positive)
        def faulty_abs(n):
            if n == 0:
                return -1
            else:
                return n if n >= 0 else n * -1

        self.assertEqual(faulty_abs(-1), 1)
        self.assertEqual(faulty_abs(1), 1)
        self.assertRaises(EnsuranceBreached, faulty_abs, 0)