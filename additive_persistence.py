n = int(input("Enter a number: "))
n = str(n)

while len(n) > 1:  
    total = 0
    for i in range(len(n)):
        total = int(n[i]) + total
    n = total
    n = str(n)
    print(n)