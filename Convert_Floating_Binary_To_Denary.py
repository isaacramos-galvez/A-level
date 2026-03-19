number = float(input("Enter a number: "))
binary_list1 = []
binary_list2 = []
def convert_binary(first_half):
    num = first_half
    if num == 0:
        binary_list1.append(0)
    while num != 0:
        if num % 2 == 1:
            binary_list1.append(1)
        elif num % 2 ==0:
            binary_list1.append(0)
        num = num // 2
    return binary_list1
def convert_floating_binary(second_half):
    num = second_half
    while num > 0 and len(binary_list2) < 16:
        temp = num * 2
        if temp >= 1:
            binary_list2.append(1)
            num = temp - 1
        elif temp < 1:
            binary_list2.append(0)
            num = temp
    return binary_list2
first_half = number // 1
second_half = number - first_half
convert_binary(first_half)
convert_floating_binary(second_half)
final_list = f"{binary_list1[::-1]}.{binary_list2}"
print(f"This number in binary is {final_list}")