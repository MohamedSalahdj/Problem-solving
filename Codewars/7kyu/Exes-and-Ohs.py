"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""
#first-solution
def xo(s):
    count_of_x = 0
    count_of_o = 0
    for letter in s:
        if letter == 'x' or letter == 'X':count_of_x+=1
        elif letter == 'o' or letter == 'O':count_of_o+=1
    return True if count_of_x == count_of_o else False

#second-solution 
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')