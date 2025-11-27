"""
Description:
    - Simple, given a string of words, return the length of the shortest word(s).
    - String will never be empty and you do not need to account for different data types.
"""


def minimum_word(words):
    min_word = len(words[0])
    for i in range(1, len(words)):
        word_length = len(words[i])
        if word_length < min_word:
            min_word=word_length
    return min_word

def find_short(s):
    return minimum_word(s.split())