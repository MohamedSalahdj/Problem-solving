"""
write me a function stringy that takes a size and returns a string of alternating 1s and 0s.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.

"""

#first-solution
def stringy(size):
    string = ''
    for i in range(size):
        string+= '1' if i%2==0 else '0'
    return string



#second-solution
def stringy(size):
    string = ''
    for i in range(1,size+1):
        string+= str(i%2)
    return string