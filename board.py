class Board:
    def __init__(self):
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""

    def get_size(self):
        # optional, return the board size (an instance size)
        return self.size

    def get_winner(self):
        # return the winner's sign O or X (an instance winner)
        return self.winner

    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can use a tuple ("A1", "B1",...) or a dictionary to obtain indexes
        # this implementation is up to you
        spots = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        index = spots.index(cell)
        self.board[index] = sign

    def isempty(self, cell):
        # return True if the cell is empty (not marked with X or O)
        spots = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        index = spots.index(cell)
        if(self.board[index] == " "):
            return True
        else:
            return False

    def isdone(self):
        done = False
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X

        # Horizontal
        for i in range(0, 3):
            if(self.board[i] == self.board[i+1] and self.board[i] == self.board[i+2] and self.board[i] in ["X", "O"]):
                self.winner = self.board[i]
                done = True

        # Vertical
        for i in range(0, 3):
            if(self.board[i] == self.board[i+3] and self.board[i] == self.board[i+6] and self.board[i] in ["X", "O"]):
                self.winner = self.board[i]
                done = True

        # Diags
        if(self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[8] in ["X", "O"]):
            self.winner = self.board[0]
            done = True

        if(self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[6] in ["X", "O"]):
            self.winner = self.board[2]
            done = True

        return done

    def show(self):
        # draw the board
        index = 0
        print("   A   B   C")
        for i in range(0, 3):
            print(" +---+---+---+\n" + str(i + 1) + "|", end=" ")
            for j in range(0, 3):
                print(self.board[index] + " |", end=" ")
                index = index + 1
            print()
        print(" +---+---+---+")
