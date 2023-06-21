""" 
    Complete the solution so that it reverses the string passed into it. 
        'world'  =>  'dlrow'
        'word'   =>  'drow'
"""
# first solution 
# def solution(string):
#     l = [letter for letter in string]
#     l.reverse()
#     return ''.join(l)

#second Solution 

def solution(string):
    i = len(string) - 1
    new_string = ''
    for _ in range(len(string)):
        new_string+= string [i]
        i-=1
    return new_string

print(solution('world'))