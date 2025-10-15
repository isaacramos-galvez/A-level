import random
import math

class vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, other):
        add_i = self.i + other.i
        add_j = self.j + other.j
        return vector(add_i, add_j)

    def find_magnitude(self):
        magnitude =  (self.i**2 + self.j**2)**0.5
        return magnitude
        
    def __sub__(self, other):
        sub_i = self.i - other.i
        sub_j = self.j - other.j
        return vector(sub_i, sub_j)
       
    def find_angle(self):
        angle = math.degrees(math.atan(self.j/self.i))
        return angle

x = random.randint(1,10)
vec1 = (x,random.randint(x,x+10))
y = random.randint(1,10)
vec2 = (y,random.randint(y,y+10))

print(vec1)
print(vec2)
print(vec1.find_magnitude())
print(vec2.find_magnitude)
print(vec1.find_angle(self))
print(vec2.find_angle(self))
print(vec1-vec2)
print(vec1+vec2)