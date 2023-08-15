"""
Write a function that checks if a given string (case insensitive) is a palindrome. 
A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, 
such as madam or racecar, the date and time 12/21/33 12:21, and the sentence: "A man, a plan, a canal – Panama".

"""
#first-solution
def is_palindrome(s):
    return s.upper() == s.upper()[::-1] 


def is_palindrome(s):
    letters = {
        "a" : "A",
        "b" : "B",
        "c" : "C",
        "d" : "D",
        "e" : "E",
        "f" : "F",
        "g" : "G",
        "h" : "H",
        "i" : "I",
        "j" : "J",
        "h" : "H",
        "i" : "I",
        "j" : "J",
        "k" : "K",
        "l" : "L",
        "m" : "M",
        "n" : "N",
        "o" : "O",
        "p" : "P",
        "q" : "Q",
        "r" : "R",
        "s" : "S",
        "t" : "T",
        "u" : "U",
        "v" : "V",
        "w" : "W",
        "x" : "X",
        "y" : "Y",
        "z" : "Z",
    }
    # convert input string to upper case 
    string_left_to_right_upper = ''
    for letter in s:
        if letter in letters:
            string_left_to_right_upper += letters[letter]
        else:
            string_left_to_right_upper+=letter
    # reverse string 
    string_right_to_left_upper = string_left_to_right_upper[::-1]

    return string_left_to_right_upper == string_right_to_left_upper