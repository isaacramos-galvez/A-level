number = int(input("Enter a number: "))
num = number
binary_list = []
while num > 0: 
    remainder = num % 2, 
    num = num // 2
    binary_list.append(remainder)
print(f"The binary equivalent of the number {number} is {binary_list[::-1]}")