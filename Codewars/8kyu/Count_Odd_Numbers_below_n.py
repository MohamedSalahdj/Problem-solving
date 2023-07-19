"""
Given a number n, return the number of positive odd numbers below n, EASY!

Examples (Input -> Output)
7  -> 3 (because odd numbers below 7 are [1, 3, 5])
15 -> 7 (because odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13])

"""
# first Slolution 
def odd_count(n):
   return int(n/2)


# Second Slolution 
def odd_count(n):
   return (n-1) / 2 if n%2 !=0 else n/2