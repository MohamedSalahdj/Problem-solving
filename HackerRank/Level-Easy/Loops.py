"""
Task
The provided code stub reads and integer, , 
from STDIN. For all non-negative integers , print .
Example

The list of non-negative integers that are less than  is . 
Print the square of each number on a separate line.

0
1
4
Input Format

The first and only line contains the integer, .



Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16

"""

#First solution 
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)

#second solution with store squre value using list comprehension 

if __name__ == '__main__':
    n = int(input())
    list_squre_number = [ i*i for i in range(0,n)]
    for i in list_squre_number:
        print(i)