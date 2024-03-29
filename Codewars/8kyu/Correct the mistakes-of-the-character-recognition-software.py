"""
Character recognition software is widely used to digitise printed texts. 
Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), 
are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. 
You only have to handle the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.

"""
# First SOlution
def correct(s):
    string_correct = ''
    for letter in s:
        if letter not in ('0', '5', '1'): string_correct+=letter 
        elif letter == '0': string_correct+= 'O'
        elif letter == '5': string_correct+= 'S'
        elif letter == '1': string_correct+= 'I'
    return string_correct
        
# Second Solution 
def correct(s):
    new_string = s.replace('0','O').replace('5','S').replace('1','I')
    return new_string

#third-solution 
def correct(s):
    list_of_char = list(s)    
    i = 0
    while i < len(list_of_char):
        if list_of_char[i] == '5':
            list_of_char[i] = 'S'
        elif list_of_char[i] == '0':
            list_of_char[i]='O'
        elif list_of_char[i] == '1':
            list_of_char[i] = 'I'
        i+=1
    return ''.join(list_of_char)



