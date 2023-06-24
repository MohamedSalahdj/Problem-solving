"""
Write a function that accepts an integer n and a string s as parameters,
and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello
"""


#first solution 
def repeat_str(repeat, string):
    return string * repeat 

#second solution 
def repeat_str(repeat, string):
    string_with_repeat = '' 
    while repeat > 0:
        string_with_repeat+= string
        repeat-= 1
    return string_with_repeat

