"""
In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples (Input -> Output)
* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9]

"""

# First_solution 
def reverse_list(l):
    return l[::-1]

# Second-solution
def reverse_list(l):
    new_list = [l[i] for i in range(len(l)-1,-1,-1)]
    return new_list

print(reverse_list([1, 2, 3, 4]))