
# In Python, you can define a class using the class keyword. A class is a blueprint 
# for creating objects

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"my name is {self.name} and i am {self.age} years old"
    
Person1 = Person("durgesh" , 20)

print(Person1.introduce())

     