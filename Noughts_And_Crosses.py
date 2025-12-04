class BoardState:
    def __init__(self):
        self.row1 = [' ', '|', ' ','|', ' ']
        self.row2 = [' ' , '|', ' ' ,'|', ' ']
        self.row3 = [' ', '|', ' ','|', ' ']
        self.column1 = [self.row1[0], self.row2[0], self.row3[0]]
        self.column2 = [self.row1[2], self.row2[2], self.row3[2]]
        self.column3 = [self.row1[4], self.row2[4], self.row3[4]]

    def display_board(self):
        print(self.row1)
        print(" ------+---------+------")
        print(self.row2)
        print(" ------+---------+------")
        print(self.row3)

    def convert_index_move(self, index_move):
        if index_move == 1:
            index_move -= 1
        elif index_move == 2:
            pass
        elif index_move == 3:
            index_move += 1
        return index_move

    def your_move(self, row_move, index_move):
        
        index_move = self.convert_index_move(index_move)
        
        while True:
            if row_move == 1:
                row = self.row1
            elif row_move == 2:
                row = self.row2
            elif row_move == 3:
                row = self.row3

            if row[index_move] == " ":
                row[index_move] = "X"
                print(f"You moved to row {row_move} and to index {index_move}")
                break
            
            print("Invalid Move")
            row_move = int(input("In which row do you want to move?"))
            index_move = int(input("Which index of the row do you want to move?"))

            index_move = self.convert_index_move(index_move)

    def computer_move(self):

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
                row = self.row1
            elif row_random == 2:
                row = self.row2
            elif row_random == 3:
                row = self.row3

            if row[index_random] == " ":
                row[index_random] = "O"
                print(f"The computer moved to row {row_random} and to index {index_random}")
                break
            
            row_random = random.randint(1, 3)
            index_random = random.randint(1, 3)
        
        if index_random == 1:
            index_random -= 1
        elif index_random == 2:
            pass
        elif index_random == 3:
            index_random += 1

while True:
    board = BoardState()
    board.display_board()
    your_row_move = int(input("In which row do you want to move?"))
    your_index_move = int(input("Which index of the row do you want to move?"))
    board.your_move(your_row_move, your_index_move)
    board.computer_move()
        
           
           
           
           
           
            # 2d list
            # class of board
            # method of placing a piece
