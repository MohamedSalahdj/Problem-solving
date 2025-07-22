"""
    You are given two sorted arrays that contain only integers. These arrays may be sorted in either ascending or descending order. 
    Your task is to merge them into a single array, ensuring that:

    The resulting array is sorted in ascending order.

    Any duplicate values are removed, so each integer appears only once.

    If both input arrays are empty, return an empty array.

    No input validation is needed, as both arrays are guaranteed to contain zero or more integers.

Examples (input -> output)
* [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

* [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

* [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]
"""

def merge_arrays(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    array = []
    i = j = 0
    
    # compare and sort two arrays 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            array.append(arr1[i])
            i +=1
            j +=1
        elif arr1[i] < arr2[j]:
            array.append(arr1[i])
            i +=1
        else:
            array.append(arr2[j])
            j +=1
    
    # Move remmains items from first array
    while i < len(arr1):
        array.append(arr1[i])
        i +=1
        
    # Move remmains items from second array
    while j < len(arr2):
        array.append(arr2[j])
        j +=1
    
    return array
    
    
print(merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]))