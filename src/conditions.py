"""
A list of built in conditions to be used in contracts.
Can be used by the module users and also helpful for testing.

The best way to extend the module is by adding conditions and
a accompaniying test.

"""

from helpers import partial, iterable_of_objtype, instance_of

is_string = partial(instance_of, str)
is_int = partial(instance_of, int)
is_float = partial(instance_of, float)
is_num = lambda n: is_int(n) or is_float(n)
is_list_of_ints = partial(iterable_of_objtype, int)
