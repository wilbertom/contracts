#Contracts - Python design by contract.

This module defines some helpful functions for performing
Contract Programming in Python. I know that Contract Programming
was first used in the Eiffel programming language. This module
will not follow everything on it(because I have never programmed
in Eiffel or read). Instead this module is my take and implementation 
of Contract Programming. It might be exactly the same or completely 
different from it. Hopefully in the future I will be able to 
learn Eiffel and follow it's implementation.

In the mean while. In this module:

A *Contract* is a list of terms that must be satisfied.

A *Term* limits a function's domain or range(input or output) to
values that satisfy a list of conditions.

A *Requirement* is a term that limits a function's domain to
values that satisfy a list of conditions.

An *Ensurance* is a term that limits another function's range to
values that satisfy a list of conditions.

A *Condition* is something that evaluates to true during a contract.

When extended to data structures, a *Contract*scan be a function that limits
the set of values a property can take.

## Usage

So what does this translate to? Above I'm being vague on purpose. Let's use
this module to implement type checking in Python.

```
from contracts import ensure, require

def is_int(n):
    return isinstance(n, int)

def is_string(s):
    return isinstance(s, str)

@require(is_int, is_string)
@ensure(is_string)
def repeat(string, n_times):
    return string * n_times

print(repeat('Hello ', 3))
'Hello Hello Hello'

print(repeat('Hello', 's'))
Boomsmahsunakskn error is raised

```

A `term` is a decorator function that takes numerous
`conditions`. `conditions` are just functions that return
a truthy(preferably `True` or `False`) value. It applies
each condition function at some point. A function decorated
in `terms` is a `contract`. 

Above our `terms` are `ensure` and `require`. We `require`
that our first parameter `is_string` and the second `is_int`.

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
def not_zero(n):
    return n != 0

def is_num(n):
    return isinstance(n, int) or isinstance(n, float)

@require(is_num, is_num)
@requre(None, not_zero)
def divide(n, by):
    return n / by

divide(5, 5) # 1
divide(5, 0) # booomaknsakjda error


```

Above we implement a function that accepts two numbers and
requires that the second parameter is `not_zero`. As opposed
to having all over your source code checks for 
`if n == 0: raise Excep...`, here we define a condition 
that can be used anywhere. Now never again will you write 
`if n == 0: raise Excep...`.

Also as a nice side effect, we get some really nice syntax that
document our functions.


## Directory Structure

```
├── LICENSE.md - MIT
├── Makefile - Ha ha yes, no C in this directory, I'm just lazy
├── README.md - This file
└── src - All the source code
    ├── conditions.py - Some built in conditions
    ├── contracts.py - The most important part. The built in contracts
    ├── helpers.py - Things that help the core. Should not be used outside.
    └── test_contracts.py - TDD. Add a test before sending PR
```
