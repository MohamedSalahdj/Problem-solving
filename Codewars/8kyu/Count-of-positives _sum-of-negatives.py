"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 
0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

"""

#first-solution 

def count_positives_sum_negatives(arr):
    Count_of_positives = [ item for item in arr if item > 0] 
    sum_of_negatives = [ item for item in arr if item < 0]
    return [len(Count_of_positives), sum(sum_of_negatives)] if len(arr) !=0 else arr