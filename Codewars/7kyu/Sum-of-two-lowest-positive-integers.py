"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
 No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.


"""
#first -solution 
def get_minimum_number(numbers):
    minimum_number = numbers[0]
    for item in numbers:
        if item < minimum_number:
            minimum_number = item
    
    return minimum_number

def sum_two_smallest_numbers(numbers):
    two_smallest_numbers = []    
    two_smallest_numbers.append(get_minimum_number(numbers))
    numbers.remove(get_minimum_number(numbers))
    two_smallest_numbers.append(get_minimum_number(numbers))
    
    return two_smallest_numbers[0] + two_smallest_numbers[-1]
    
#second-solution
def sum_two_smallest_numbers(numbers):
    if numbers[0] < numbers[1]:
        minimum_number_one = numbers[0]
        minimum_number_two = numbers[1]
    else:
        minimum_number_one = numbers[1]
        minimum_number_two = numbers[0]
    for i in range(2,len(numbers)):
        if numbers[i] < minimum_number_one:
            minimum_number_two = minimum_number_one
            minimum_number_one = numbers[i]
        elif numbers[i] < minimum_number_two:
            minimum_number_two = numbers[i]
    return minimum_number_one + minimum_number_two
        
#third-solution
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return sum(numbers[:2])