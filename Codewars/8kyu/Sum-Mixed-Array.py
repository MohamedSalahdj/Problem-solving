"""
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.


"""

#first_solution
def sum_mix(arr):
    sum = 0
    for i in arr:
        if isinstance(i, str):
            sum += int(i)
        else:
            sum+=i
    return sum


#secnd_solution with built in function
def sum_mix(arr):
    return sum(map(int, arr))