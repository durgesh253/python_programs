# 25) Explain Inheritance in Python with an example? What is init? Or What
# Is A Constructor In Python?

# nheritance is a fundamental concept in object-oriented programming (OOP) that 
# allows a new class (subclass or derived class) to inherit
#  properties and behaviors from an existing class (superclass or base class).


class Animal:
    def __init__(self , name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says mewoo!"
    
dog = Dog("buddy")
cat = Cat("mimi")

print(dog.speak())
print(cat.speak())

 