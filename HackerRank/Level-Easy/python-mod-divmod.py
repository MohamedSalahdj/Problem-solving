"""
One of the built-in functions of Python is divmod, which takes two arguments  and  and returns a tuple containing the quotient of  first and then the remainder .

For example:

>>> print divmod(177,10)
(17, 7)
Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

Task
Read in two integers,  and , and print three lines.
The first line is the integer division  (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: .
The third line prints the divmod of  and .

Input Format
The first line contains the first integer, , and the second line contains the second integer, .

Output Format
Print the result as described above.

Sample Input

177
10
Sample Output

17
7
(17, 7)

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
div_two_input = a//b
reminder = a % b

print(div_two_input)
print(reminder)
print((div_two_input, reminder))