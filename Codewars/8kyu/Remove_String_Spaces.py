"""

Write a function that removes the spaces from the string, then return the resultant string.

Examples:

Input -> Output
"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
"8aaaaa dddd r     " -> "8aaaaaddddr"

"""

#First solution 
def no_space(x):
    l = x.split()
    return "".join(l)

#second slution 
def no_space(x):
    string_without_space = ''
    for letter in x:
        if letter !=' ':
            string_without_space += letter
    return string_without_space