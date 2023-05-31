"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  

"""


def swap_case(s):
    l_words = s.split()
    string_after_convert =''
    for word in l_words:
        w = ''
        for letter in word:
            if letter.isupper():
                w+=str.lower(letter)
            else:
                w+=str.capitalize(letter)
        string_after_convert+= w+' '
    return string_after_convert
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

