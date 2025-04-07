"""
Define a method named countCharOccurrences or count_char_occurrences 
that accepts a string and a char as inputs and returns the number of times the char occurs in the string as an int.
"""

def count_char_occurrences(strng, char):
    char_count = 0
    for i in strng:
        if i == char:
            char_count += 1
    return char_count