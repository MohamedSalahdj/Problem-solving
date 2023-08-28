"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "

"""

def double_char(s):
    string_with_double_char = ''
    for letter in s:
        string_with_double_char+= letter*2
    return string_with_double_char