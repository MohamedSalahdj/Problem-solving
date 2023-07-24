"""
Write a function to convert a name into initials.
This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

"""

# First Solution
def abbrev_name(name):
    List_of_word = name.split()
    return f"{List_of_word[0][0].upper()}.{List_of_word[1][0].upper()}"