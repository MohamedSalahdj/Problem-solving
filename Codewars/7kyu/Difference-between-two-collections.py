"""
Find the difference between two collections.
The difference means that either the character is present in one collection or it is present in other, but not in both.
Return a sorted list with the difference.

The collections can contain any character and can contain duplicates.
"""
def diff(a, b):
    list_with_differnce = []
    for item in a:
        if item not in b and item not in list_with_differnce:
            list_with_differnce.append(item)
    for item in b:
        if item not in a and item not in list_with_differnce:
            list_with_differnce.append(item)
    list_with_differnce.sort()
    return list_with_differnce