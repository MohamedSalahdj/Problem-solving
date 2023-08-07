"""
You will be given a list of strings. You must sort it alphabetically 
(case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

"""


def two_sort(array):
    array.sort()
    first_item = array[0]
    
    string_with_star = ''
    for i in range(len(first_item)):
        string_with_star+=first_item[i]
        if i == len(first_item)-1:
            break
        string_with_star+='***'
    return string_with_star


