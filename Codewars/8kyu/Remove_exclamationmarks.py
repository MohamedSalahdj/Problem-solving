"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""
# first solution 
def remove_exclamation_marks(s):
    new_string = ''
    for letter in s:
        if letter !='!':
            new_string+=letter
    return new_string

#second solution ---> with replace method 
def remove_exclamation_marks(s):
    return s.replace('!','')

