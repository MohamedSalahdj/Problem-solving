"""
You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle (but not at beginning or end). 
The length of the strings, before and after the colon, are random.

Your job is to return a list of two strings (in the same order as the original list), 
but with the characters after each colon swapped.

Examples
["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]
"""

def cut_tail(word):
    for i in range(len(word)):
        if word[i] == ':':
            temp = word[i+1:]
            word=word[:i+1]
            break
    return word,temp

def tail_swap(strings):
    word_one = strings[0]
    word_two = strings[-1]
    head1, tail1 = cut_tail(word_one)
    head2, tail2 = cut_tail(word_two)
    return [head1+tail2, head2+tail1]