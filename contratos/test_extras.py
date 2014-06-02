"""
test_extras.py
Wilberto Morales
wilbertomorales777@gmail.com

Testing of other stuff that helps the core.

"""

import unittest
from .helpers import flip
from .conditions import is_int, is_string, is_float, is_num


class TestHelpers(unittest.TestCase):
    """
    Not all in the helpers is tested, because
    of time. However anything new from now on
    must be tested.
    """

    def test_flip(self):
        def divide(x, y):
            return x / y

        self.assertEqual(divide(100, 10), flip(divide)(10, 100))


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
