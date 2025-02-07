"""
Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

    1450   -> 145
    960000 -> 96
    1050   -> 105
    -1050  -> -105
    0      -> 0
Note: Zero should be left as it is.
"""

def remove_zero_ending(num):
    num_without_zero = ''
    for i in range(len(num)-1, 0, -1):
        if num[i] != '0':
            num_without_zero = num[0: i+1]
            break            
    return int(num_without_zero)

def no_boring_zeros(n):
    if n == 0:
        return n
    return remove_zero_ending(str(n))