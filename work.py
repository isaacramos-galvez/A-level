parentheses = input("Enter a string of parentheses")

def find_parentheses(string):
    count = 0
    for char in string:
        if len(string) > 100:
            print("This length of string is too long")
            break
        elif len(string) < 100:
            if char == "(":
                count = count + 1
            elif char == ")":
                count = count - 1
                if count < 0:
                    return False
                    break
            else:
                break
        if count == 0:
            return True
        elif count != 0:
            return False
    
check = find_parentheses(parentheses)
print(check)