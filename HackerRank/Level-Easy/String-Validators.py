if __name__ == '__main__':
    s = input()
    #check if s has any alphanumeric characters.
    i = 0
    while i <len(s):
        if s[i].isalnum():
            print("True")
            break
        if i == len(s)-1:
            print("False")
        i+=1
        
    #check if s has any alphabetical characters
    i = 0
    while i <len(s):
        if s[i].isalpha():
            print("True")
            break
        if i == len(s)-1:
            print("False")
        i+=1
        
    #check if s has any digits
    i = 0
    while i <len(s):
        if s[i].isdigit():
            print("True")
            break
        if i == len(s)-1:
            print("False")
        i+=1
        
    #check if s has any lowercase characters.
    i = 0
    while i <len(s):
        if s[i].islower():
            print("True")
            break
        if i == len(s)-1:
            print("False")
        i+=1
       
    #check if s has any uppercase characters.
    i = 0
    while i <len(s):
        if s[i].isupper():
            print("True")
            break
        if i == len(s)-1:
            print("False")
        i+=1
        