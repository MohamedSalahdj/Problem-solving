"""

Create a function that accepts a string and a single character,
and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", "o")  ==>  1
("Hello", "l")  ==>  2
("", "z")       ==>  0
str_count("Hello", 'o'); // returns 1
str_count("Hello", 'l'); // returns 2
str_count("", 'z'); // returns 0
"""


def str_count(strng, letter):
    count_of_leter = 0
    
    if letter in strng:
        for l in strng:
            if l == letter:
                count_of_leter+=1
                
    return count_of_leter