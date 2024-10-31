"""
As part of this kata, you need to find the length of the sub-array that begins and ends with the specified number.

For example, if the array arr is [0, -3, 7, 4, 0, 3, 7, 9], finding the length of the sub-array that begins and ends with 7s would return 5.

For sake of simplicity, there will only be numbers (positive or negative) in the supplied array.

If there are less or more than two occurrences of the number to search for, return 0.

"""

def length_of_sequence(arr, n):
    if arr.count(n) != 2:
        return 0
    first_index = arr.index(n)
    last_index = arr.index(n, first_index + 1)
    return last_index - first_index + 1
