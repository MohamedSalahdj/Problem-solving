"""
Description:
Write a method, that will get an integer array as parameter and will process every number from this array.

Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

    Example
    [4,3,9,7,2,1] -> [2,9,3,49,4,1]
Notes
    The input array will always contain only positive numbers, and will never be empty or null.
"""
import math

def has_square(number):
    return math.sqrt(number) == int(math.sqrt(number))

def square_or_square_root(arr):
    new_arr = [math.sqrt(number) if has_square(number) else number**2 for number in arr]
    return new_arr
    

print(square_or_square_root([4, 3, 9, 7, 2, 1 ]))
print(square_or_square_root([100, 101, 5, 5, 1, 1]))