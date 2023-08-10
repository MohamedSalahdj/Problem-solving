"""
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
"""
def replace_exclamation(s):
    new_string = ''
    for letter in s:
        if letter in ('a','e','i','o','u','A','E','I','O','U'):
            new_string+='!'
        else:
            new_string+=letter
    return new_string