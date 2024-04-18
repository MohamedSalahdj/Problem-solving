"""
Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

Example:
For input: [3, 4, 4, 3, 6, 3]

remove the 3 at index 0
remove the 4 at index 1
remove the 3 at index 3
Expected output: [4, 6, 3]

More examples can be found in the test cases.

Good luck!

"""

#first_solution
def solve(arr): 
    i = 0
    while i < len(arr):
        if arr[i] in arr[i+1:]:
            arr.remove(arr[i])
        else:
            i+=1
    return arr


#second-solution
def solve(arr): 
    list_without_duplicate = [ arr[i] for i in range(len(arr))  if arr[i] not in arr[i+1:] ]
    return list_without_duplicate


