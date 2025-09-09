from sys import getsizeof
import random

test_set = [0, 5, 66, 42]
for i in range (1,5):
    print(test_set, type(test_set), getsizeof(test_set))
    test_set.append(random.randint(1,100))






