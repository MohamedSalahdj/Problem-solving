"""
DESCRIPTION:

Task
Given a string, return if a given letter always appears immediately before another given letter.

Worked Example
("he headed to the store", "h", "e") ➞ True

# All occurences of "h": ["he", "headed", "the"]
# All occurences of "h" have an "e" after it.
# Return True
Examples
("i found an ounce with my hound", "o", "u") ➞ True

("we found your dynamite", "d", "y") ➞ False
Notes
All sentences will be given in lowercase.

"""
#first-solution
# def best_friend(txt, a, b):
#     two_letter = a+b
#     s = 0
#     ss = 0
#     if a !=b:
#         for word in txt.split():
#             if a in word:
#                 s+=1
#                 if two_letter in word:
#                     ss+=1
#         return s==ss
#     else:
#         return False
            


def best_friend(txt, a, b):
    number_of_first_letter = 0
    number_of_two_letter = 0
    l = txt.split()
    print(l)
    for word in l:
        if a in word:
            number_of_first_letter+=1
            if a+b in word:
                number_of_two_letter+=1
    return number_of_first_letter == number_of_two_letter 

print(best_friend('abcdee', 'e', 'e'))

# print("hello")