"""
    Given a month as an integer from 1 to 12, 
        return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; 
    month 6 (June), is part of the second quarter; 
    and month 11 (November), is part of the fourth quarter.

Constraint:

1 <= month <= 12
"""
# first solution 
def quarter_of(month):
    if month in range(1,4):
        return 1
    elif month in range(4,7):
        return 2 
    elif month in range(7,10):
        return 3
    return 4

#second solution 
def quarter_of(month):
    if month/3 <=1:
        return 1
    elif month/3 > 1 and  month/3 <= 2 :
        return 2
    elif month/3 > 2 and month/3  <=3 :
        return 3
    return 4

#Third Solution 
def quarter_of(month):
    return 1 if month < 4 else 2 if month < 7 else 3 if month < 10 else 4
