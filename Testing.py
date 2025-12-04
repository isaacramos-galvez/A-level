import random

row1 = [' ', '|', ' ','|', ' ']
row2 = [' ' , '|', ' ' ,'|', ' ']
row3 = [' ', '|', ' ','|', ' ']
column1 = [row1[0], row2[0], row3[0]]
column2 = [row1[2], row2[2], row3[2]]
column3 = [row1[4], row2[4], row3[4]]

def display_board():
    print(row1)
    print(" ------+---------+------")
    print(row2)
    print(" ------+---------+------")
    print(row3)

def your_move():
    row_move = int(input("In which row do you want to move?"))
    index_move = int(input("Which index of the row do you want to move?"))
    if index_move == 1:
        index_move -= 1
    elif index_move == 2:
        pass
    elif index_move == 3:
        index_move += 1
    
    while True:
        if row_move == 1:
            row = row1
        elif row_move == 2:
            row = row2
        elif row_move == 3:
            row = row3

        if row[index_move] == " ":
            row[index_move] = "X"
            print(f"You moved to row {row_move} and to index {index_move}")
            break
        
        print("Invalid Move")
        row_move = int(input("In which row do you want to move?"))
        index_move = int(input("Which index of the row do you want to move?"))

        if index_move == 1:
            index_move -= 1
        elif index_move == 2:
            pass
        elif index_move == 3:
            index_move += 1

def computer_move():

    row_random = random.randint(1, 3)
    index_random = random.randint(1, 3)
    
    if index_random == 1:
        index_random -= 1
    elif index_random == 2:
        pass
    elif index_random == 3:
        index_random += 1

    while True:
        if row_random == 1:
            row = row1
        elif row_random == 2:
            row = row2
        elif row_random == 3:
            row = row3

        if row[index_random] == " ":
            row[index_random] = "O"
            print(f"The computer moved to row {row_random} and to index {index_random}")
            break
        
        row_random = random.randint(1, 3)
        index_random = random.randint(1, 3)


    if row_random == 1:
        row1[index_random] = "O"
    elif row_random == 2:
        row2[index_random] = "O"
    elif row_random == 3:
        row3[index_random] = "O"   
    
    if index_random == 1:
        index_random -= 1
    elif index_random == 2:
        pass
    elif index_random == 3:
        index_random += 1

def check_winner():
    if row1[0] == "X":
        if row1[2] == "X":
            if row1[4] == "X":
                print("X wins!")
                display_board()
                exit()
    if row2[0] == "X":
        if row2[2] == "X":
            if row2[4] == "X":
                print("X wins!")
                display_board()
                exit()
    if row3[0] == "X":
        if row3[2] == "X":
            if row3[4] == "X":
                print("X wins!")
                display_board()
                exit()
    if row1[0] == "O":
        if row1[2] == "O":
            if row1[4] == "O":
                print("O wins!")
                display_board()
                exit()
    if row2[0] == "O":
        if row2[2] == "O":
            if row2[4] == "O":
                print("O wins!")
                display_board()
                exit()
    if row3[0] == "O":
        if row3[2] == "O":
            if row3[4] == "O":
                print("O wins!")
                display_board()
                exit()
    if column1[0] == "X":
        if column1[1] == "X":
            if column1[2] == "X":
                print("X wins!")
                display_board()
                exit()
    if column2[0] == "X":
        if column2[1] == "X":
            if column2[2] == "X":
                print("X wins!")
                display_board()
                exit()
    if column3[0] == "X":
        if column3[1] == "X":
            if column3[2] == "X":
                print("X wins!")
                display_board()
                exit()
    if column1[0] == "O":
        if column1[1] == "O":
            if column1[2] == "O":
                print("O wins!")
                display_board()
                exit()
    if column2[0] == "O":
        if column2[1] == "O":
            if column2[2] == "O":
                print("O wins!")
                display_board()
                exit()
    if column3[0] == "O":
        if column3[1] == "O":
            if column3[2] == "O":
                print("O wins!")
                display_board()
                exit()
    if row1[0] == "X":
        if row2[2] == "X":
            if row3[4] == "X":
                print("X wins")
                display_board()
                exit()
    if row1[4] == "X":
        if row2[2] == "X":
            if row3[0] == "X":
                print("X wins")
                display_board()
                exit()
    if row1[0] == "O":
        if row2[2] == "O":
            if row3[4] == "O":
                print("O wins")
                display_board()
                exit()
    if row1[4] == "O":
        if row2[2] == "O":
            if row3[0] == "O":
                print("O wins")
                display_board()
                exit()
win = False
while win == False:
    display_board()
    your_move()
    check_winner()
    computer_move()
    check_winner()
    