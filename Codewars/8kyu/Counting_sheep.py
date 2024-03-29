"""
Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
"""

#First Solution 
def count_sheeps(sheep):
    sum_of_sheep = 0
    for i in sheep:
        if i == True:
            sum_of_sheep+=1
    return sum_of_sheep


#second Solution 
def count_sheeps(sheep):
    number_of_true = 0
    for i in sheep:
        if i:
            number_of_true+=1
    return number_of_true

#Third Solution  with list comprehension

def count_sheeps(sheep):
    number_of_true = [ 1  for i in sheep if i]
    return len(number_of_true)