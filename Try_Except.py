usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']

class EnemyError(Exception):
    pass


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    try:
        number = int(usernumber)
    except ValueError:
        print("Your input is a string, please enter a integer")
        return False
    if number == 5:
        raise EnemyError("ALERT!")
    try:
        print("Welcome", usernames[number], "user number", number,".")
    except IndexError:
        print("Please enter a valid number within the range")
        return False
    try:
        division = 301 / number
    except ZeroDivisionError:
        print("Division by zero is not possible try again with number not being equal to zero")
        return False

    print(f"301 divided by {number} = {division}")

    

while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)