"""
The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.

However, there is a bug in the method that needs to be resolved.
"""

# First Solution
def kata_13_december(lst): 
    i = 0
    while i < len(lst):
        if lst[i]%2==0: 
            lst.remove(lst[i])
        else:
            i+=1
    return lst

print(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]))


# Second solution 
def kata_13_december(lst): 
    return [ item for item in lst if item%2 !=0 ] 