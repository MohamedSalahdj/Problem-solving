"""
DESCRIPTION:
The notorious Captain Schneider has given you a very straightforward mission.
Any data that comes through the system make sure that only non-special characters see the light of day.

Create a function that given a string, retains only the letters A-Z (upper and lowercase), 0-9 digits, and whitespace characters. 
Also, returns "Not a string!" if the entry type is not a string.

"""


# first_solution
def nothing_special(st):
    if not isinstance(st, str):
        return "Not a string!"
    normal_string = ''
    all_character = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '\t', '\n', '\r', '\x0b', '\x0c'
    ]
    for letter in st:
        if letter in all_character:
            normal_string += letter
    return normal_string


#second_solution
import re
def nothing_special(st):
    if not isinstance(st, str):
        return "Not a string!"
    retained_data = re.sub(r'[^A-Za-z0-9\s]', '', st)
    return retained_data