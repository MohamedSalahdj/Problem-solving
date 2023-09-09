"""
DESCRIPTION:
Task
Create a function that always returns True for every item in a given list. However, 
if an element is the word "flick", switch to always returning the opposite boolean value.

Examples
["codewars", "flick", "code", "wars"] ➞ [True, False, False, False]

["flick", 11037, 3.14, 53] ➞[False, False, False, False]

[False, False, "flick", "sheep", "flick"] ➞ [True, True, False, False, True]
Notes
"flick" will always be given in lowercase.
A list may contain multiple flicks.
Switch the boolean value on the same element as the flick itself.

"""

# First-solution
def flick_switch(lst):
    l = []
    t = True
    for item in lst:
        if item != 'flick':
            l.append(t)
        else:
            t = not t
            l.append( t)
    return l
            


#second-solution

def flick_switch(lst):
    l , bool = [], True
    for item in lst:
        if item == 'flick':
            bool = not bool
        l.append(bool)
    return l