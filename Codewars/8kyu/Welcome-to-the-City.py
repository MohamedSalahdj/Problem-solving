""" 

Create a method that takes as input a name, city, and state to welcome a person.
 Note that name will be an array consisting of one or more values that should be joined together with one space between each, 
 and the length of the name array in test cases will vary.

Example:

['John', 'Smith'], 'Phoenix', 'Arizona'
This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!
"""



#first-solution 
def say_hello(name, city, state):
    return "Hello, " + ' '.join(name) + '! ' + 'Welcome to ' + city + ', ' + state +'!'


#second-solution 
def say_hello(name, city, state):
    return f'Hello, {" ".join(name)}! Welcome to {city}, {state}!'

#third_solution
def say_hello(names, city, state):
    #extract name from names without built-in function 
    full_name = '' 
    for i in range(len(names)-1):
        full_name+=names[i] + ' '
    full_name+=names[-1]
        
    return f'Hello, {full_name}! Welcome to {city}, {state}!'
