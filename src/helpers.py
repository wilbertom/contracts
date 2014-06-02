"""
helpers.py
Wilberto Morales
wilbertomorales777@gmail.com

Some functions to help create conditions and other
things.

"""
from functools import partial

def flip(f):
    """
    Returns a new function who takes
    two parameters flipped from f, but does
    the same as f.

    :param f: a function
    :return: a function like f but with reversed arguments
    """
    def f_flipped(y, x):
        return f(x, y)

    return f_flipped

def iterable_of_objtype(obj_type, l):
    if l == []:
        return False

    for i in l:
        if not isinstance(i, obj_type):
            return False

    return True

# a function that when partialy applied
# makes type checkers really quickly
instance_of = flip(isinstance)

# creates exceptions given a string name, and base class
# exceptions for lazy people
exception_fun = lambda name, base: type(name, (base,), {})
