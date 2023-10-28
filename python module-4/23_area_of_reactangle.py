class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area_rectangle(self):
        return self.length * self.width
    
rectangle1 = Rectangle(5,9)

area = rectangle1.area_rectangle()
print(f"area of rectangele is :{area}")
