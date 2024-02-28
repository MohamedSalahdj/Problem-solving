"""
Given 2 string parameters, show a concatenation of:

the reverse of the 2nd string with inverted case; e.g Fish -> HSIf
a separator in between both strings: @@@
the 1st string reversed with inverted case and then mirrored; e.g Water -> RETAwwATER 
** Keep in mind that this kata was initially designed for Shell, I'm aware it may be easier in other languages.**
"""

#Fish ----> HSIf
#Water ---> RETAwwATER
# HSIf@@@RETAwwATER 

#first-solution
def reverse_and_mirror(s1, s2):
    new_s1 = ''
    new_s2 = ''
    for letter in s2:
        if letter.isupper():
            new_s1+=letter.lower()
        else:
            new_s1+=letter.upper()
    
    for letter in s1:
        if letter.isupper():
            new_s2+=letter.lower()
        else:
            new_s2+=letter.upper()
            
    return new_s1[::-1] + "@@@" + new_s2[::-1] + new_s2