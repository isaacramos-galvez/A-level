filename = 'file_text.txt'
def return_file():
    open(filename, 'r')
    text = filename.readlines()
    print('text')
    if text == "":
        print("this file is empty")
    else:
        print(text)
    file.close()

def menu():
    file_chosen = input("What file do you want to edit?")
    open(file_chosen, 'w')
    input_text = input("What do you want to right to the file?")
    file_chosen.write(input_text)

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
        

    