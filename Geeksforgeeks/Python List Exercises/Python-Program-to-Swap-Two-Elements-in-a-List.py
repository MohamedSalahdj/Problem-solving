"""
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

Examples:  

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]

Swap Two Elements in a List using comma assignment 
Since the positions of the elements are known, we can simply swap the positions of the elements. 

"""

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]

    return list

print(swapPositions( [23, 65, 19, 90], 1, 2))
