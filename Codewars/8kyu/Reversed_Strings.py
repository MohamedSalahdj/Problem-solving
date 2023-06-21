""" 
    Complete the solution so that it reverses the string passed into it. 
        'world'  =>  'dlrow'
        'word'   =>  'drow'
"""
# first solution 
def solution(string):
    l = [letter for letter in string]
    l.reverse()
    return ''.join(l)
