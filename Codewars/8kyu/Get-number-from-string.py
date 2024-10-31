"""
    Write a function which removes from string all non-digit characters and parse the remaining to number. \
    E.g: "hell5o wor6ld" -> 56

    Function:

    getNumberFromString(s)
"""

def get_number_from_string(st):
    num = ''
    list_of_number = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    for letter in st:
        if letter in list_of_number:
            num +=letter
    return int(num)