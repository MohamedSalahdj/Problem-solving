"""
You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.

if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.

Example:
arguments: 1, 2, "+"
should return 3

arguments: 1, 2, "&"
should return "unknown value"

arguments: 1, "k", "*"
should return "unknown value"

"""

import operator

def calculator(x, y, op):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    func = operations.get(op)
    return func(x, y) if op in operations and isinstance(x, int) and isinstance(y,int) else "unknown value"