"""
Description:
    This is your first potion class in Hogwarts and professor gave you a homework to figure out what color potion will turn 
    into if he'll mix it with some other potion. All potions have some color that written down as RGB color 
    from [0, 0, 0] to [255, 255, 255]. To make task more complicated teacher will do few mixing 
    and after will ask you for final color. Besides color you also need to figure out what volume will have potion after final mix.

Task
    Based on your programming background you managed to figure that after mixing two potions colors will mix as if mix two RGB colors. 
    For example, if you'll mix potion that have color [255, 255, 0] and volume 10 with one that have color [0, 254, 0] and volume 5, you'll get new potion with color [170, 255, 0] and volume 15. 
    So you decided to create a class Potion that will have two properties: 
    color (a list (a tuple in Python) with 3 integers) and volume (a number), and one method mix that will accept another Potion and return a mixed Potion.

"""

from math import ceil

class Potion:
    def __init__(self, color: list | tuple, volume: int):
        self.color = color 
        self.volume = volume
    
    def mix(self, other) -> "Potion":
        result = []
        volume_summation = self.volume + other.volume
        for i, j in zip(self.color, other.color):
            temp = ceil(((i * self.volume) + (j * other.volume)) / volume_summation)
            result.append(temp)
        
        return Potion(type(self.color)(result), volume_summation)