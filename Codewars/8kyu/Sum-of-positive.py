"""
You get an array of numbers,
return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""

def positive_sum(arr):
    arr_of_positive_number = [number for number in arr if number > 0]
    
    return sum(arr_of_positive_number)
