"""
Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.

Examples:

Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]

"""
#first-solution
def distinct(seq):
    arr_without_dulicate = []
    for item in seq: 
        if item not in arr_without_dulicate:
            arr_without_dulicate.append(item)
            
    return arr_without_dulicate