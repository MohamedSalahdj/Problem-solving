"""
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. 
If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. 
If there are no good ideas, as is often the case, return 'Fail!'.
"""

#first_Solution 
def well(x):
    couont_good_ideas = x.count('good')
    if couont_good_ideas in (1, 2):
        return 'Publish!'
    elif couont_good_ideas > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'

#second_soution 
def well(x):
    return 'I smell a series!' if x.count('good') > 2 else 'Fail!' if x.count('good') == 0 else 'Publish!'
