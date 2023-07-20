"""
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.

"""

# first-solution

def find_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) !=0 else 0