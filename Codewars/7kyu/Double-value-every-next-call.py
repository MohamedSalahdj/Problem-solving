"""
Description:
    This kata is about static method that should return different values.
    On the first call it must be 1, on the second and others - it must be a double from previous value.
    Look tests for more examples, good luck :)w
"""


class Class:
    value = None
    
    @staticmethod
    def get_number():
        if Class.value is None:
            Class.value = 1
        else:
            Class.value *= 2
        return Class.value