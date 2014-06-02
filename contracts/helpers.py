"""
helpers.py
Wilberto Morales
wilbertomorales777@gmail.com

Some functions to help create conditions and other
things.

"""


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

def all_satisfy(fun, iterable):
    """
    Walks the iterable and returns false
    if applying fun to the element is false.
    If all return true then returns true.

    :param fun: function passed to all elements of iterable
    :param iterable: iterable collection of elements
    :return: true or false
    """
    for i in iterable:
        if not fun(i):
            return False
    else:
        return True

# a function that when partially applied
# makes type checkers really quickly
instance_of = flip(isinstance) # @not-tested

# creates exceptions given a string name, and base class
# exceptions for lazy people
exception_fun = lambda name, base: type(name, (base,), {}) # @not-tested

