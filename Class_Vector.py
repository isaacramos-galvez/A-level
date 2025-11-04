import random
import math

class Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __str__(self):
        return f"{self.i}i + {self.j}j"

    def __add__(self, other):
        add_i = self.i + other.i
        add_j = self.j + other.j
        return Vector(add_i, add_j)

    def __sub__(self, other):
        sub_i = self.i - other.i
        sub_j = self.j - other.j
        return Vector(sub_i, sub_j)
       
    def magnitude(self):
        magnitude =  round(math.sqrt(self.i**2 + self.j**2),2)
        return magnitude
        
    def find_angle(self):
        angle = round(math.degrees(math.atan(self.j/self.i)),2)
        return angle

    def mul(self, scalar):
        
        scalar = int(input("What is the value of the scalar you want to input?"))
        for i in 

    def __rmul_(self, scalar):
        mul_veci = vec1 * scalar
        mul_vecj = vec2 * scalar
        return mul_veci
        return mul_vecj

x = random.randint(1,10)
vec1 = Vector(x,random.randint(x,x+10))
y = random.randint(1,10)
vec2 = Vector(y,random.randint(y,y+10))

def test_vector():
    pass

print(vec1)
print(vec2)
print(vec1.magnitude())
print(vec2.magnitude())
print(vec1.find_angle())
print(vec2.find_angle())
print(vec1 * random.randint(1,10))
print(vec2 * random.randint(1,10))
print(vec1-vec2)
print(vec1+vec2)