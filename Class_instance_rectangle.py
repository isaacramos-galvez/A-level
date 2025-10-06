import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area
    
    def get_perimeter(self):
        self.perimeter = (self.width * 2) + (self.height *2)
        return self.perimeter
    
    def find_width(self):
        width = self.width
        return width
    
    def find_height(self):
        height = self.height
        return height
    
    def calculate_diagonal(self):
        diagonal = math.sqrt((self.height ** 2)+(self.width ** 2))
        return diagonal

input_width = int(input("What is the width of the rectangle?"))
input_height = int(input("What is the height of the rectangle?"))
shape = Rectangle(input_width, input_height)
print("The area of the rectangle is",shape.get_area(),"cm^2")
print("The perimeter of the rectangle is",shape.get_perimeter(),"cm")
print("The width of the shape is",shape.find_width(),"cm")
print("The height of the shape is",shape.find_height(),"cm")
print("The length of the diagonal is",shape.calculate_diagonal(),"cm")