'''
Do you remember the old mobile display keyboards? Do you also remember how inconvenient it was to write on it?
Well, here you have to calculate how many keystrokes you have to do for a specific word.

This is the layout:


Given a string, return the number of keystrokes necessary to type it. 
You can assume that the input will entirely consist of characters included in the mobile layout (lowercase letters, digits, and the symbols * and #).

Examples
"*#"       =>  2 (1 + 1)
"123"      =>  3 (1 + 1 + 1)
"abc"      =>  9 (2 + 3 + 4)
"codewars" => 26 (4 + 4 + 2 + 3 + 2 + 2 + 4 + 5)

'''

#first_Solution

def mobile_keyboard(s):
    mobile_keys = {
    '1': 1, '2': 1, '3': 1,
    '4': 1, '5': 1, '6': 1,
    '7': 1, '8': 1, '9': 1,
    '' : 0, '*': 1, '#': 1, '0' : 1,
    'a': 2, 'b': 3, 'c': 4,
    'd': 2, 'e': 3, 'f': 4,
    'g': 2, 'h': 3, 'i': 4,
    'j': 2, 'k': 3, 'l': 4,
    'm': 2, 'n': 3, 'o': 4,
    'p': 2, 'q': 3, 'r': 4, 's': 5,
    't': 2, 'u': 3, 'v': 4,
    'w': 2, 'x': 3, 'y': 4, 'z': 5
}
    number_of_keystrokes = 0
    for char in s:
        number_of_keystrokes += mobile_keys[char]
    return number_of_keystrokes