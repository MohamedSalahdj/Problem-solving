"""
Given a string of digits, 
you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.

Note: input will never be an empty string
"""

# first-solution
def fake_bin(x):
    string_without_any_number_graeter_or_lower_than5 = ''
    for i in x :
        if int(i) < 5 :string_without_any_number_graeter_or_lower_than5+='0'
        else:string_without_any_number_graeter_or_lower_than5+='1'
    return string_without_any_number_graeter_or_lower_than5
            

#second-solution with list-comprehesion
def fake_bin(x):
    l = ['0' if i < '5' else '1' for i in x ]
    return ''.join(l)