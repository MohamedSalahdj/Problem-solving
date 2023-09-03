"""
DESCRIPTION:
Task
Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. 
Note: The result should be a boolean value, instead of a string.
The opposite means: All letters of the two strings are the same, but the case is opposite.
you can assume that the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are empty then you should return false/False.

Examples (input -> output)
"ab","AB"     -> true
"aB","Ab"     -> true
"aBcd","AbCD" -> true
"AB","Ab"     -> false
"",""         -> false

"""










#first-solution
def is_opposite(s1,s2):
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
        "A" : "a",
        "B" : "b",
        "C" : "c",
        "D" : "d",
        "E" : "e",
        "F" : "f",
        "G" : "g",
        "H" : "h",
        "I" : "i",
        "J" : "j",
        "K" : "k",
        "L" : "l",
        "M" : "m",
        "N" : "n",
        "O" : "o",
        "P" : "p",
        "Q" : "q",
        "R" : "r",
        "S" : "s",
        "T" : "t",
        "U" : "u",
        "V" : "v",
        "W" : "w",
        "X" : "x",
        "Y" : "y",
        "Z" : "z",
    }
        i = 0
        while i<len(s1):
            if letters[s1[i]] != s2[i]:
                return False 
            i+=1
        return True if len(s1) !=0 else False 
        

#second-solution 
def is_opposite(s1,s2):
    return  s1.swapcase() == s2 and s1!=""