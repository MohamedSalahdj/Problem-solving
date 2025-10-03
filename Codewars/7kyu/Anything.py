"""
What is the answer to life the universe and everything

Create a function that will make anything true

    anything({}) != [],          'True'
    anything('Hello') < 'World', 'True'
    anything(80) > 81,           'True'
    anything(re) >= re,          'True'
    anything(re) <= math,        'True'
    anything(5) == ord,          'True'

"""


def anything(thing):
    """
        try to return anything else :)
    """
    class Truthy:
        def __eq__(self, other): return True
        def __ne__(self, other): return True
        def __lt__(self, other): return True
        def __le__(self, other): return True
        def __gt__(self, other): return True
        def __ge__(self, other): return True
    
    return Truthy()


# test cases
print(anything({}) != []) # Truthy().__ne__([])
print(anything('Hello') < 'World') # Truthy().__lt__('World')
print(anything(80) > 81) # Truthy().__gt__(81)
