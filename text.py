# multiplication table game

count = 1
number = int(input("Enter a number between 1 and 12"))

while number > 12 or number < 1 or number == str(""):
    number = int(input("Enter a valid number between 1 and 12"))

max = int(input("Please enter the number you wish to times up to"))
while count <= max:
    print(f"{count}*{number} is",number * count)
    count = count + 1


