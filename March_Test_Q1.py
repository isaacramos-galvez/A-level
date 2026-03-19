value = int(input("Enter a integer(0-99): "))
operation = input("Calculate additive of multiplicative persistence ( a or m)? ")
count = 0
while value > 9:
    if operation == "a": value = (value // 10) + (value % 10)
    else: value = (value // 10) * (value % 10)
    count = count + 1
print(f"The persistence is: {count}")