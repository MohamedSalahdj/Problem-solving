"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9

"""
#First Solution 
def square_sum(numbers):
    sum_of_number = 0
    for number in numbers:
        sum_of_number+= number*number
    return sum_of_number

#Second Solution with list comprehension 
def square_sum(numbers):
    sum_of_square_number  = [ number*number for number in numbers ]
    return sum(sum_of_square_number)