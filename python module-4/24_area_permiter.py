import math


class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def compute_area(self):
        return math.pi * self.radius**2
    
    def compute_perimeter(self):
        return 2 * math.pi * self.radius
    
circle1 = Circle(6)

area = circle1.compute_area()
perimeter = circle1.compute_perimeter()

print(f"The area of circle is {area:.2f}")

print(f"The perimeter of circle is :  {perimeter:.2f}")