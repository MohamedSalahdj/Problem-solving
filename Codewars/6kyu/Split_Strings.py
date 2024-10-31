"""
DESCRIPTION:
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

"""

#first_solution 
def solution(s):
    l = []
    string = '' 
    if len(s) %2 == 0:
        for letter in s:
            string+= letter #a
            if len(string) == 2:
                l.append(string)
                string = ''
        return l
    else:
        for letter in range(0,len(s)): 
            string+= s[letter]
            if len(string) == 2:
                l.append(string)
                string = ''
            if letter == len(s) - 1:
                l.append(s[letter]+'_')
        return l