"""
Create a function that takes 2 integers in form of a string as an input, 
and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"
"""
##first-solution 
def sum_str(a, b):
    if a == '' and b == '': 
        a,b = 0,0
    elif a == '' : 
        a = 0
    elif b == '' : 
        b = 0
    return str(int(a) + int(b))


#second solution 
def sum_str(a, b):
    return str(int(a) + int(b)) if a and b else a or b or '0'
