"""
Write a function which converts the input string to uppercase.
"""
s = 'mohamed'
s_new = s[::-1]
print(s_new)

# SecondSolution 
def make_upper_case(s):
    string_with_upper_case = ''
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
    for letter in s:
        if letter in letters:
            string_with_upper_case+= letters[letter]
        else:
            string_with_upper_case+=letter
    return string_with_upper_case