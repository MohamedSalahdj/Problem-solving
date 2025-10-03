""" 
    I don't like writing classes like this:

    class Animal:
        def __init__(self, name, species, age, health, weight, color):
            self.name = name
            self.species = species
            self.age = age
            self.health = health
            self.weight = weight
            self.color = color
    Give me the power to create a similar class like this:

    Animal = make_class("name", "species", "age", "health", "weight", "color")
"""

def make_class(*args):
    class Animal(object):
        def __init__(self, *values):
            for key, value in zip(args, values):
                setattr(self, key, value)
    
    return Animal