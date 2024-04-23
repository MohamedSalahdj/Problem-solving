"""
DESCRIPTION:
Continuation to Python's Dynamic Classes #1 Kata.

- That name changing function is awesome! - Timmy heard from his boss - but would it not be possible to hide somehow that function in classes itself?

Timmy was thinking about it for while than decided to contact with his guru - you - and ask about it.
You offered him to build class that could be inherited, and could provide some class method to modify name of already existing classes. The new class should be named as

ReNameAbleClass
and the special one method should be

change_class_name
Like before, be sure that new solution will allow only names with alphanumeric chars (upper & lower letters plus digits), but starting only with upper case letter.

Moreover, for testing purposes, he want new class to have

__str__
method which will be returning string like "Class name is: MyClass" for MyClass.



Too easy? Check Python's Dynamic Classes #3 Kata and make sure that solved Python's Dynamic Classes #1 Kata.
"""

class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        if not new_name[0].isupper() or not  new_name.isalnum():
            raise ValueError("Class Name Not vaild")
        cls.__name__ = new_name
        
    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"
