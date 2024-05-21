"""
DESCRIPTION:
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

"""
#first_solution
def find_outlier(integers):
    num_odd  = []
    num_even = []
    for i in integers:
        if i%2 ==0:
            num_odd.append(i)
        else:
            num_even.append(i)
    if len(num_odd) > 1:
        for i in num_even:
            return i
    else:
        for i in num_odd:
            return i

#second_solution
def find_outlier(integers):
    even_number = []
    odd_number = []
    for number in integers:
        if number % 2 == 0:
            even_number.append(number)
        else:
            odd_number.append(number)
    return odd_number[0] if len(odd_number) == 1 else even_number[0]
