"""
In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

Examples:
[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []

"""
#first-solution
def two_highest(arg1):
    s = list(set(arg1))
    s.sort(reverse=True)
    return s[:2]


#second-solution
def remove_dublicate(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                return remove_dublicate(l[i+1:])
    return l

def inverse_sort_list(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] < l[j]:
                temp = l[j]
                l[j] = l[i]
                l[i] = temp
    return l
def two_highest(arg1):
    arg1 = remove_dublicate(arg1)
    print(arg1)
    arg1 = inverse_sort_list(arg1)
    return arg1[:2]


print(two_highest([15, 20, 20, 17]))