"""
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

    a.add(b)      # should return a new Vector([4, 6, 8])
    a.subtract(b) # should return a new Vector([-2, -2, -2])
    a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
    a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
    a.add(c)      # raises an exception

If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:
    a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' 
    (in Python, this is a __str__ method, so that str(a) == '(1,2,3)'. In PHP, this is __toString magic method)
    an equals method, to check that two vectors that have the same components are equal
    Note: the test cases will utilize the user-provided equals method.
"""

class Vector:
    def __init__(self, components):
        self.components = components
    
    def _validate(self, other):
        if len(self.components) != len(other.components):
            raise Exception("Vectors must be of equal length")
            
    def _common(self, other, op):
        self._validate(other)
        return Vector([ op(x, y) for x, y in zip(self.components, other.components)])
        
    def add(self, other):
        return self._common(other, lambda x, y: x + y)
    
    def subtract(self, other):
        return self._common(other, lambda x, y: x -y)
    
    def dot(self, other):
        self._validate(other)
        return sum([ x * y for x, y in zip(self.components, other.components)])
    
    def norm(self):
        return sum(x * x for x in self.components) ** 0.5
    
    def equals(self, other):
        return self.components == other.components
    
    def __str__(self):
        return "(" + ",".join(str(x) for x in self.components) + ")"
        