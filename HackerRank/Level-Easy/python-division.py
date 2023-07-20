"""
Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.

Example
a = 3
b = 5

- The result of the integer division .
-  The result of the float division is .

Print:
0
0.6

Input Format

The first line contains the first integer, .
The second line contains the second integer, .

Output Format

Print the two lines as described above.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333
Language
Python 3
More
1234
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b,'\n',a/b)


Line: 4 Col: 25

Test against custom input
Congratulations!

You have passed the sample test cases. Click the submit button to run your code against all the test cases.


Sample Test case 0
Input (stdin)
4
3
Your Output (stdout)
1 
 1.3333333333333333
Expected Output
1
1.33333333333


"""


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b,'\n',a/b)