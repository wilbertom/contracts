"""
A list of built in conditions to be used in contracts.
Can be used by the module users and also helpful for testing.

The best way to extend the module is by adding conditions and
a accompaniying test.

"""

from functools import partial
from collections import Iterable
from helpers import instance_of, all_satisfy

# type checking
is_string = partial(instance_of, str)
is_int = partial(instance_of, int)
is_float = partial(instance_of, float)
is_num = lambda n: is_int(n) or is_float(n)
is_tuple = partial(instance_of, tuple)  # @not-tested
is_list = partial(instance_of, list)  # @not-tested
is_iterable = partial(instance_of, Iterable)  # @not-tested

# specific numeric sets
is_positive = lambda n: n > 0  # @not-tested
is_non_negative = lambda n: n >= 0  # @not-tested
is_natural = lambda n: is_int(n) and is_positive(n)  # @not-tested
is_natural_0 = lambda n: is_int(n) and is_non_negative(n)  # @not-tested
is_negative = lambda n: is_num(n) and not is_non_negative(n)  # @not-tested
is_even = lambda n: n % 2 == 0  # @not-tested
is_odd = lambda n: not is_even(n)  # @not-tested
is_zero = lambda n: n == 0  # @not-tested
not_zero = lambda n: not is_zero(n)  # @not-tested

# convenience sets
are_ints = partial(all_satisfy, is_int)  # not-tested
