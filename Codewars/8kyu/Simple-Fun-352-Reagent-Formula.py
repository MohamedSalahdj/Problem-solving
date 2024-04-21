def isValid(formula):
    if 7 in formula or 8 in formula:
        if 5 in formula and 6 in formula:
            return True
        if 1 in formula and 2 not in formula:
            return True
        if 3 in formula and 4 not in formula:
            return True  
        else: 
            return False
        
    else:
        return False

print(isValid([1,3,7]))  
print(isValid([7,1,2,3]))

print(isValid([1,3,5,7]))

print(isValid([1,5,6,7,3]))

print(isValid([5,6,7]))

print(isValid([5,6,7,8]))

print(isValid([6,7,8]))

print(isValid([7,8]))