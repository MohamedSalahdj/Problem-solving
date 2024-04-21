"""
Sum all the numbers of a given array ( cq. list ), 
except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, 
even if there are more than one with the same value.

Mind the input validation.

Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6

"""
#first-soluton 
def sum_array(arr):
    if arr not in ([],None) and len(arr) != 1 :
        arr.remove(min(arr))
        arr.remove(max(arr))
        return sum(arr)
    else:
        return 0

#second-solution 
def sum_array(arr):
    return 0 if arr == None or len(arr) < 3 else sum(arr) - (max(arr) + min(arr))
        