"""
Given a string and an array of indices, rearrange the characters of the string so that each character is placed at the position specified by the corresponding index in the array.

Example
    input: "abcd", [0, 3, 1, 2]
    output: "acdb"
Explanation
    The character 'a' is placed at index 0.

    The character 'b' is placed at index 3.

    The character 'c' is placed at index 1.

    The character 'd' is placed at index 2.

Notes
    The string and the array will be of equal length.

The string will contain valid characters (A-Z, a-z, or 0-9);
the array will contain valid indices.

"""


def scramble(strng, array):
    new_arr = [ 0 for _ in range(len(array)) ]
    j = 0
    for i in array:
        new_arr[i] = strng[j]
        j+=1
    return "".join(new_arr)


print(scramble('sc301s', [4,0,3,1,5,2])) # c0s3s1