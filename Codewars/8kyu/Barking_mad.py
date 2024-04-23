"""
Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.

snoopy.bark() #return "Woof"
scoobydoo.bark() #undefined
Use method prototypes to enable all Dogs to bark.
"""


class Dog ():
  def __init__(self, breed):
    self.breed = breed
    
  def bark(self):
        return "Woof"

    
    
snoopy = Dog("Beagle")

snoopy.bark()

scoobydoo = Dog("Great Dane")
scoobydoo.bark()

