"""
test_contracts.py
Wilberto Morales
wilbertomorales777@gmail.com

This was my first project developed using somewhat TDD(thanks to @nwinklareth).

"""

import unittest
from .contracts import require, ensure, RequirementBreached, \
    ContractParamsError, EnsuranceBreached
from .conditions import is_int, is_string, is_num, \
    not_zero, are_ints, is_positive


# functions to help during the tests

@require(is_string)
@ensure(is_string)
def greet(name):
    return "hello %s" % name


@require(are_ints)
@ensure(is_int)
@ensure(is_positive)
def faulty_sum(ns):
    return sum(ns)


@require(is_int, is_int)
@ensure(is_int)
def raise_to(n, power):
    return n ** power


@require(None, is_int)
@ensure(is_int)
def times(o, n):
    return o * n


@require(is_num, is_num)
@require(None, not_zero)
@ensure(is_num)
def divide(n, by):
    return n / by


# TODO: decorating should trow the error instead of calling the function
@require(is_string, is_int, is_num)
def hello(name):
    return "Hello sneaky %s" % name


class TestContracts(unittest.TestCase):
    """
    Tests for a contract's requirement.
    """

    def test_return(self):

        h = greet("Wil")
        self.assertEqual(h, "hello Wil")

        self.assertRaises(RequirementBreached, greet, 1)

    def test_ints(self):

        # should return the value of 'faulty_sum' if requirements met
        self.assertEqual(faulty_sum([1, 2, 3, 4, 5]), 15)
        # or raise an error if not met
        self.assertRaises(RequirementBreached, faulty_sum, ['A', 'B', 'C'])

    def test_many_params(self):

        # should be able to decorate a function
        # with multiple params
        self.assertEqual(raise_to(3, 3), 27)

    def test_nullable_param(self):

        self.assertEqual(times(3, 3), 9)
        self.assertRaises(RequirementBreached, times, 'a', 0.1)

    def test_multiple(self):

        self.assertEqual(divide(4, 4), 1)
        self.assertRaises(RequirementBreached, divide, 4, 0)
        self.assertRaises(RequirementBreached, divide, '3', 3)

    def test_with_too_many_args(self):

        self.assertRaises(ContractParamsError, hello, 'Wil')
        # TODO: do with ensurance

    def test_with_too_little_params(self):

        self.assertRaises(ContractParamsError, hello, 'Wil')
        # TODO: do with ensurance

    def test_breaking_first_ensurance(self):

        self.assertRaises(EnsuranceBreached, times, 'a', 3)

    def test_breaking_second_ensurance(self):

        self.assertRaises(EnsuranceBreached, faulty_sum, [-1, -2, -3])
