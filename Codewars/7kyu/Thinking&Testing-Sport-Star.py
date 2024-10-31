''' 
            problem name : Thinking & Testing : Sport Star
DESCRIPTION:
    No Story

    No Description

    Only by Thinking and Testing

    Look at result of testcase, guess the code!

'''

#first_solution
def testit(act, s):
    result = ''
    j = '|'
    r = '_'
    
    for i in range(len(act)):
        if act[i] == 'jump' and s[i] == j:
            result+=j
        elif act[i] == 'jump' and s[i]!= j:
            result+='x'
        elif act[i] == 'run' and s[i] == r:
            result+=r
        elif act[i] == 'run' and s[i] != r:
            result+='/'
    return result
   
#second_solution 
def testit(act, s):
    dict_result = {
        'run_': '_',
        'run|': '/',
        'jump|': '|',
        'jump_': 'x'
    }
    result = ''
    for i in range(len(act)):
        result +=dict_result[act[i]+s[i]]
    return result 