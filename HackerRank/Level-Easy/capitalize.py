
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = s.split()
    for i in range(len(l)):
        l[i] = l[i].capitalize()
    s = ' '.join(l)
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()








# Other solution 


#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    return ' '.join([ name.capitalize() for name in s.split()])
    # return ' '.join([ name.capitalize() if name.isalnum() else name for name in s.split()])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()




