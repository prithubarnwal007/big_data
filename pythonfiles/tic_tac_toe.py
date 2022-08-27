
class tictactoefucntions:
    X = "X"
    O = "O"
    EMPTY = " "
    TIE = "TIE"
    NUM_SQUARES = 9

    def display_instructions(self):
        print(
            """
            Welcome to a game of Tic-Tac-Toe. You will be playing against an AI.
            You will be able to make your move on the board by entering any number from 0 - 8.
            The number will correspond to the board position as shown below:
    
                              0 | 1 | 2
                              ---------
                              3 | 4 | 5
                              ---------
                              6 | 7 | 8
    
            May the best player win!\n
            """
        )

    def ask_question(self,question):
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response

    def ask_number(self, question, low, high):
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

    def pieces(self):
        go_first = self.ask_question("Do you want to go first? (y/n): ")
        if go_first == "y":
            print("\nGreat! Let the game begin.")
            human = self.X
            computer = self.O
        else:
            print("\nAlright. I will go first. Wish you all the best!")
            computer = self.X
            human = self.O
        return computer, human

    def new_board(self):
        board = []
        for square in range(self.NUM_SQUARES):
            board.append(self.EMPTY)
        return board

    def display_board(self,board):
        print("\n\t", board[0], "|", board[1], "|", board[2])
        print("\t", "---------")
        print("\n\t", board[3], "|", board[4], "|", board[5])
        print("\t", "---------")
        print("\n\t", board[6], "|", board[7], "|", board[8], "\n")

    def legal_moves(self, board):
        moves = []
        for square in range(self.NUM_SQUARES):
            if board[square] == self.EMPTY:
                moves.append(square)
        return moves

    def winner(self,board):
        WAYS_TO_WIN = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))
        for row in WAYS_TO_WIN:
            if board[row[0]] == board[row[1]] == board[row[2]] != self.EMPTY:
                winner = board[row[0]]
                return winner
        if self.EMPTY not in board:
            return self.TIE
        return None

    def human_move(self,board, human):
        legal = self.legal_moves(board)
        move = None
        while move not in legal:
            move = self.ask_number("Where will you move? (0-8): ", 0, self.NUM_SQUARES)
            if move not in legal:
                print("\nUn oh, looks like that square is already occupied. Choose another one.\n")
        print("Fine...")
        return move

    def computer_move(self,board, computer, human):
        board = board[:]

        BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

        print("I shall take square number", end=" ")

        for move in self.legal_moves(board):
            board[move] = computer
            if self.winner(board) == computer:
                print(move)
                return move
            board[move] = self.EMPTY

        for move in self.legal_moves(board):
            board[move] = human
            if self.winner(board) == human:
                print(move)
                return move
            board[move] = self.EMPTY

        for move in BEST_MOVES:
            if move in self.legal_moves(board):
                print(move)
                return move

    def next_turn(self,turn):
        if turn == self.X:
            return self.O
        else:
            return self.X

    def congrat_winner(self,the_winner, computer, human):
        if the_winner != self.TIE:
            print(the_winner, "won!\n")
        else:
            print("It's a tie!\n")

        if the_winner == computer:
            print("Well, I won this round.  \n"
                  "Better luck next time.")

        elif the_winner == human:
            print("You know what they say. \n"
                  "Winner Winner Chicken Dinner!")

        elif the_winner == self.TIE:
            print("It's a TIE. \n"
                  "Better luck next time.")

