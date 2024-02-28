"""
Write a function

vowel_2_index
that takes in a string and replaces all the vowels [a,e,i,o,u] with their respective positions within that string.
E.g:

vowel_2_index('this is my string') == 'th3s 6s my str15ng'
vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
vowel_2_index('') == ''
Your function should be case insensitive to the vowels.

"""

# using while loop 
def vowel_2_index(string):
    new_string = ''
    i = 0
    while i < len(string):
        if string[i].lower() in ('a','e','i','o','u'):
            new_string+=f'{i+1}'
        else:
            new_string+=string[i]
        i+=1
    return new_string


#using for loop
def vowel_2_index(string):
    new_string = ''
    for i in range(len(string)):
        if string[i].lower() in ['a','e','i','o','u']:
            new_string+=str(i+1)
        else:
            new_string+=string[i]
    return new_string
