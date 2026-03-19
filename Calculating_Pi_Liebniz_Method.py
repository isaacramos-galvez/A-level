pi = 1 - 1/3 + 1/5
for i in range(1000000000):
    pi = pi - (1/(4*(i)+7)) + (1/(4*(i)+9))
print(pi*4)