"""
    You will get an array of numbers.

    Every preceding number is smaller than the one following it.

    Some numbers will be missing, for instance:

    [-3,-2,1,5] //missing numbers are: -1,0,2,3,4
    Your task is to return an array of those missing numbers:

    [-1,0,2,3,4]

"""

def find_missing_numbers(arr):
    if not arr:
        return []
    list_missing_numbers =[]
    start_number = arr[0]
    end_number = arr[-1]
    i = 1
    for number in range(start_number+1, end_number):
        if number ==  arr[i]:
            i+=1
        else:
            list_missing_numbers.append(number)
    return list_missing_numbers
            