x = int(input("Enter a integer greater than 1: "))
product = 1
factor = 0
while product < x:
    factor += 1
    product = product * factor

if x == product:
    product = 1
    for N in range(1,factor + 1):
        product = product * N
        print(N)
else:
    print("no result")
