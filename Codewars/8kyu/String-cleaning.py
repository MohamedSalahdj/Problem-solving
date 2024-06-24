"""
Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning in the text of old novels to your database.
At first it seems to capture words okay, but you quickly notice that it throws in a lot of numbers at random places in the text.

Examples (input -> output)
'! !'                 -> '! !'
'123456789'           -> ''
'This looks5 grea8t!' -> 'This looks great!'
Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers. 
Your program will take in a string and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.

"""




def string_clean(s):
    """
        Function will return the cleaned string
    """
    list_of_number = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    
    cleaned_string = ''
    
    for letter in s:
        if letter not in list_of_number:
            cleaned_string +=letter
            
    return cleaned_string