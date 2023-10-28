# Instantiation: Instantiation is the process of creating an instance of a class. 
#  It typically involves calling a special method called a constructor 
#  (often named __init__ in Python) to set up the initial state of the object
#  and allocate memory for it.

class Person:
    def __init__(self, name, age):
        self.name = name
        self,age = age

person1 = Person("Durgesh", 20)

