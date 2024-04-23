"""
Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:

- Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!

Tim sighed, he already knew it's gonna be a long day.
Few hours later, boss came again:
Much better - he said - but now I want to change that class name to SecondUsefulClass,

and went off. Although Timmy had no idea why changing name is so important for his boss,
he realized, that it's not the end, so he turned to you, his guru, to help him and asked you to prepare some function,
which could change name of given class.
Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers),
but starting only with upper case letter. In other case it should raise an exception.
Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that,
that Timmy yet has to learn them.


To easy? Check Python's Dynamic Classes #2 Kata and Python's Dynamic Classes #3 Kata.

"""

class MyClass:
    pass

def class_name_changer(cls, new_class_name):
    if not new_class_name[0].isupper():
        raise ValueError("The First Character in new class name must start with upper case letter")
    
    if not new_class_name.isalnum():
        raise ValueError("New class name must contain only alphanumeric characters")
    
    cls.__name__ = new_class_name
    
    