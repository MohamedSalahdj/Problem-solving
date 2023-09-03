"""
DESCRIPTION:
Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

Note: if this seems too simple for you try the next level
"""

#first-solution 
def print_array(arr):
    sequance = ''
    for i in range(len(arr)-1):
        sequance+=str(arr[i]) +','
    sequance+=str(arr[-1])
    return sequance


#second-solution 
def print_array(arr):
    return ",".join(map(str, arr))