"""
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.

"""

# First solution 

def boolean_to_string(b):
    return "True" if b == 1 else "False"

# Second solution 
def boolean_to_string(b):
    return "True" if b else "False"

#Third Solution 
def boolean_to_string(b):
    return f"{b}"