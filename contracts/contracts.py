"""
contracts.py
Wilberto Morales
wilbertomorales777@gmail.com

This module defines some helpful functions for performing
Contract Programming in Python. I know that Contract Programming
was first used in the Eiffel programming language. This module
will not follow everything on it(because I have never programmed
in Eiffel). Instead this module is my take and implementation of
it. It might be exactly the same or completely different from it.
Hopefully in the future I will be able to learn Eiffel and
follow it's implementation.

In the mean while. In this module:

A *Contract* is a list of terms that must be satisfied.

A *Term* limits a function's domain or range(input or output) to
values that satisfy a list of conditions.

A *Requirement* is a term that limits a function's domain to
values that satisfy a list of conditions.

An *Ensurance* is a term that limits another function's range to
values that satisfy a list of conditions.

A *Condition* is something that evaluates to true during a contract.

When extended to data structures Contract can be a function that limits
the set of values a property can take.

"""

from helpers import exception_fun

ContractError = exception_fun('ContractError', Exception)
ContractBreached = exception_fun('ContractBreached', ContractError)
RequirementBreached = exception_fun('RequirementBreached', ContractBreached)
EnsuranceBreached = exception_fun('EnsuranceBreached', ContractBreached)
ContractParamsError = exception_fun('ContractParamsError', ContractError)

def term(term_handler):
    """
    Black magic.

    :param term_handler: a function that has the signature
    f(conditions, fun, *args)
    :return: a function that can be used to decorate other functions
    """

    def contract_term(*conditions):

        def fun_with_conditions(f):

            # TODO: should be f(*args, *kwargs)
            def new_fun(*args):

                return term_handler(conditions, f, *args)

            return new_fun

        return fun_with_conditions

    return contract_term


@term
def require(conditions, fun, *args):
    """
    Require makes sure that all parameters
    passed to fun are valid under a condition.

    A condition can be None if you don't want an
    argument to be bothered.

    For example arg[0] must satisfy conditions[0].
    conditions[0](arg[0]) and so on.

    :param conditions: an iterable of condition_functions
    :param fun: a function
    :param args: arguments for fun
    :return: fun(*args) if all pass their condition
    """

    if len(conditions) != len(args):
        raise ContractParamsError('Contract is faulty. conditions and args'
                                  'have different lengths.')
    for c, a in zip(conditions, args):
        if c is not None and not c(a):
            raise RequirementBreached('Term condition: %s breached by'
                                      '%s(%s, _)' % (c, fun, args))
    else:
        return fun(*args)

@term
def ensure(conditions, fun, *args):
    """
    Ensure makes sure that the return values
    of a function meet it's conditions.
    Values in plural because Python's functions
    can return lists and tuples.

    For example returned[0] must satisfy conditions[0].
    conditions[0](returned[0]) and so on.
    Where returned is the result of fun(*args).


    :param conditions: an iterable of condition_functions
    :param fun: a function to watch over
    :param args: arguments for fun
    :return: the result of fun(*args) if it satisfies it's conditions
    """
    ret = fun(*args)

    for c in conditions:
        if not c(ret):
            raise EnsuranceBreached('Term ensurance: %s breached by'
                                    'return value %s' % (c, ret))
    else:
        return ret