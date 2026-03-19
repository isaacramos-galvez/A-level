from numpy import random # used over import random as allows for a float between 0 and 1 to be returned
within_circle = 0
for i in range(1000000):
    x =  random.rand()
    y =  random.rand()
    if (x*x) + (y*y) < 1:
        within_circle += 1
print((within_circle/1000000)*4)


