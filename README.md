# Contratos - Python contract programming

This module defines some helpful functions for performing
Contract Programming in Python. I know that Contract Programming
was first used in the Eiffel programming language. This module
will not follow everything on it(because I have never programmed
in Eiffel or read Eiffel). Instead this module is my take and implementation
of Contract Programming. It might be exactly the same or completely 
different from it. Hopefully in the future I will be able to 
learn Eiffel and follow it's implementation.

Meanwhile, in this module:

A *Contract* is a list of terms that must be satisfied.

A *Term* limits a function's domain or range(input or output) to
values that satisfy a list of conditions.

A *Requirement* is a term that limits a function's domain to
values that satisfy a list of conditions.

An *Ensurance* is a term that limits a function's range to
values that satisfy a list of conditions.

A *Condition* is something that evaluates to true during a contract.

When extended to data structures, a *Contract* can limit the set of
values a property can take.

## Installation

```
git clone https://github.com/wilbertom/contracts
cd ./contratos
make install
```

If running `make` worries you or you don't have it installed in your system,
just run:

```
python setup.py install
```

The module has *no requirements*, except running `python 3.4`. Everything
should work on `2.7`, but it is not the targeted version.

## Usage

So what does this translate to? Above I'm being vague on purpose. Let's use
this module to implement type checking in Python.

```
from contratos.contracts import ensure, require

def is_int(n):
    return isinstance(n, int)

def is_string(s):
    return isinstance(s, str)

@require(is_string, is_int)
@ensure(is_string)
def repeat(string, n_times):
    return string * n_times

print(repeat('Hello ', 3)) # 'Hello Hello Hello'

print(repeat('Hello', 's')) # Boomsmahsunakskn error is raised

```

A `term` is a decorator function that takes numerous
`conditions`. `conditions` are just functions that return
a truthy(preferably `True` or `False`) value. It applies
each condition function at some point. A function decorated
in `terms` is a `contract`. 

Above our `terms` are `ensure` and `require`. We `require`
that our first parameter `is_string` and the second `is_int`.
So our conditions are `is_string` and `is_int`.

We `ensure` that the first(and only in this case) return value
`is_string`.

Besides all the bad methaphors I hope you can see the power
behind this. These `terms` create invariants under which we
can program. 

The second call to repeat above would raise an error
because the second parameter didn't satisfy `is_string`.

Type checking is just one reason to use this, but as we
know having functions that don't need to specify a type
is most of the time good. So here is another example.

```
from contratos.contracts import require

def not_zero(n):
    return n != 0

def is_num(n):
    return isinstance(n, int) or isinstance(n, float)

@require(is_num, is_num)
@require(None, not_zero)
def divide(n, by):
    return n / by

print(divide(5, 5)) # 1.0
divide(5, 0) # booomaknsakjda error

```

Above we implement a function that accepts two numbers and
requires that the second parameter is `not_zero`. As opposed
to having all over your source code checks for 
`if n == 0: raise Excep...`, here we define a condition 
that can be used anywhere. Now never again will you write 
`if n == 0: raise Excep...`.

Also as a side effect, we get some really nice syntax that
documents our functions.

A function can have more that one `ensure` and more than one
`require`. Make sure that the return value and input parameters
match the signature of your `conditions`.

## Built-in Conditions

Since some conditions will be so common, the module defines a
few for convenience, *feel free to propose more*. You can create
an issue it and tag it with the condition label.

Here are some already defined. They can be found under
`contratos.conditions`.

```

# type checking
is_string = partial(instance_of, str)
is_int = partial(instance_of, int)
is_float = partial(instance_of, float)
is_num = lambda n: is_int(n) or is_float(n)
is_bool = partial(instance_of, bool)  # @not-tested
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
are_ints

```

To see the updated list take a look inside the `contratos/conditions.py` file.

## Running Tests

I tried developing this project using `TDD`. I broke the practice because it was
my first time. Still some tests exists and all the source code will be
tested in the future.

```
make tests
```

Or:

```
python -m unittest discover contratos.test_contracts
python -m unittest discover contratos.test_extras
```

As of now it looks like it's running the tests twice. I'm
just figuring how this stuff works.

## Directory Structure

```
├── LICENSE.md - MIT
├── Makefile - Ha ha yes, no C in this directory, I'm just lazy
├── README.md - This file
└── contratos - All the source code
    ├── conditions.py - Some built in conditions
    ├── contracts.py - The most important part. The built in contracts
    ├── helpers.py - Things that help the core. Should not be used outside.
    └── test_contracts.py - TDD. Add a test before sending PR
```
