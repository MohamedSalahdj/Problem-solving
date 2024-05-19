"""
DESCRIPTION:
At the annual family gathering, the family likes to find the oldest living family member’s age and the youngest family member’s age and calculate the difference between them.

You will be given an array of all the family members' ages, in any order. 
The ages will be given in whole numbers, so a baby of 5 months, will have an ascribed ‘age’ of 0.
Return a new array (a tuple in Python) with [youngest age, oldest age, difference between the youngest and oldest age].

"""

def difference_in_ages(ages):
    oldest_member = ages[0]
    youngest_age = ages[0]
    for i in range(1, len(ages)):
        if oldest_member < ages[i]:
            oldest_member = ages[i]
        elif youngest_age > ages[i]:
            youngest_age = ages[i]
    return (youngest_age, oldest_member, oldest_member-youngest_age)