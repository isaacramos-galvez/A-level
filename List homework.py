list = ["Alp", "Carter", "Longyu", "Samuel", "Teo", "Ryan", "Oscar", "George", "Isaac", "Kevin", "Henry", "Henry", "Papa", "Aidan", "Thomas"]

for i in range(3):
    name = input("Type in a name: ")
    list.append(name)

print(list)
print(f"The third name in the list is {list[2]}")
print(f"The last seven items in the list are {list[-7:]}")

list = []
for i in range(5):
    number = int(input("Enter a number"))
    if number == "":
        print("Enter a valid input")
    elif number == str:
        print("Enter a valid number")
    else:
        list.append(number)
        list.sort()
        print(f"The list is",list)
        print("   ---------   ")
        
    
    

print(f"The smallest number in the list is {min(list)}")
print(f"The biggest number in the list is {max(list)}")
print("The total of all the numbers in the list is",sum(list))
print("The average of all the numbers in the list is",sum(list)/ len(list))




