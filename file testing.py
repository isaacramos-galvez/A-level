filename = "Computer Science Homework/file_text.txt"
def return_file():
    with open("Computer Science Homework/file_text.txt", 'r') as file:
        text  = file.readlines()
        print(text)
        if text == "":
            print("this file is empty")
        else:
            print(text)
    file.close()

def menu():
    file_chosen = input("What file do you want to edit?")
    open(file_chosen, 'w')
    if file_chosen == False:
        print("That file cannot be found")
    else:
        input_text = input("What do you want to right to the file?")
        file_chosen.write(input_text)
        return_file()

choice_continue = "yes"
while choice_continue == "yes":
    return_file()
    menu()
    result  = input("Do you want to continue?")
    if result != "yes":
        choice_continue != "yes"
        return_file()
        file.close()
        break
        

    