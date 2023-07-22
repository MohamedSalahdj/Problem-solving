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
        