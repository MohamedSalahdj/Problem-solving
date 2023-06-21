"""
The first century spans from the year 1 up to and including the year 100,
the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
"""

# first solution 
def century(year):
    if year in range(1,101):
        return 1
    elif year%100 == 0:
        return year/100
    return int(year/100)+1


#Second solution with Ternary Operators 

def century(year):
   
    return 1 if year in range(1, 101)  else year/100 if year%100 == 0 else int(year/100)+1  