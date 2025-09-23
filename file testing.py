filename = 'file_text.txt'
def return_file():
    open(filename, 'r')
    text = filename.readlines()
    if text == "":
        print("this file is empty")
    else:
        print(text)
    file.close()

def write_to_file():
    open(filename, 'w')
    input_text = input("What do you want to write to the file?")
    filename.write(input_text)
    
    
choice_continue = "yes"
while choice_continue == "yes":
    return_file()
    write_to_file()
    result  = input("Do you want to continue?")
    if result != "yes":
        choice_continue != "yes"
        return_file()
        file.close()
        break
        

    