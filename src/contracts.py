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

A *Contract* limits a function's domain or range(input or output) to
values that satisfy a list of conditions.

A *Requirement* is a type of contract that limits a function's
domain to values that satisfy a list of conditions.

An *Ensurance* is a type of contract that limits another function's
range to values that satisfy a list of conditions.

A *Condition* is something that evaluates to true during a contract.

When extended to data structures Contract can be a function that limits
the set of values a property can take.

"""

exception_fun = lambda name, base: type(name, (base,), {})
ContractBreached = exception_fun('ContractBreached', Exception)
RequirementBreached= exception_fun('RequirementError', ContractBreached)

def new_contract(contract_handler):
    def contract(conditions):
        def fun_with_conditions(f):

            def new_fun(*args):
                return contract_handler(conditions, f, *args)



            return new_fun

        return fun_with_conditions

    return contract


@new_contract
def require(conditions, fun, *args):
    if conditions(*args):
        return fun(*args)
    else:
        raise RequirementBreached('Condition %s breached by'
                                  '%s(%s, _)' % (conditions, fun, args))

