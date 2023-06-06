"""
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .

Constraints
--------------------
Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
------------------------
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""
# First solution using 'textwrap' module 
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# Second solution using loop and mod
def wrap(string, max_width):
    s = ''
    i = 0
    for letter in string:
        i +=1
        s +=letter
        if i %max_width ==0:
            s+='\n'
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)