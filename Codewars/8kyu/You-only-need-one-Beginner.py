"""
You will be given an array a and a value x.
All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.

"""

# First Solution 
def check(seq, elem):
    return elem in seq

# Second Solution 


def check(seq, elem):
    for item in seq:
        if item == elem : return True
    return False