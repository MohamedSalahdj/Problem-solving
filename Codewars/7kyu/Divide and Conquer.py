"""
    Given a mixed array of number and string representations of integers, 
    add up the non-string integers and subtract the total of the string integers.
    Return as a number.
"""



def div_con(x):
    total_int_number = 0
    string_number = 0 
    for number in x:
        if type(number) == str:
            string_number += int(number)
        else:
            total_int_number+=number
    return total_int_number-string_number