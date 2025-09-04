# multiplication table game
import random
mode = input("Do you want to do test mode or check mode?")
if mode == "check":
    count = 1
    number = int(input("Enter a number between 1 and 12"))
    while number > 12 or number < 1:
        number = int(input("Enter a valid number between 1 and 12"))
        
        max = int(input("Please enter the number you wish to times up to"))
        while count <= max:
            print(f"{count}*{number} is",number * count)
            count += 1
elif mode == "test":
    score = 0
    current_question = 1
    questions = int(input("How many questions do you want to answer?"))
    while current_question > questions:
        num1 = int(input("What times table do you want to test?"))
        num2 = random.randint(1,12)
        answer = input(f"What is {num1}*{num2}?")
        correct = num1 *num2
        if 
