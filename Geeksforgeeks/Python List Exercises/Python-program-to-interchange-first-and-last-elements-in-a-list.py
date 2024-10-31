"""
Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]

"""

def swap_list(arr):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
    return arr


print(swap_list([12, 35, 9, 56, 24]))