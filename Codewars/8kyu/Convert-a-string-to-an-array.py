"""
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""

# first-solution with built-in-function
# def string_to_array(s):
#     return s.split(" ") 

#Second-solution without split
def string_to_array(s):
    l = []
    i = 0
    word = ''
    while i < len(s):
        if s[i] != ' ':
            word+=s[i]
        else:
            l.append(word)
            word = ''
        i+=1
    l.append(word)
    return l

