from tic_tac_toe import tictactoefucntions


if __name__ == '__main__':
    tictactoefunctions_obj = tictactoefucntions()
    tictactoefunctions_obj.display_instructions()
    computer, human = tictactoefunctions_obj.pieces()
    turn = tictactoefunctions_obj.X
    board = tictactoefunctions_obj.new_board()
    tictactoefunctions_obj.display_board(board)

    while not tictactoefunctions_obj.winner(board):
        if turn == human:
            move = tictactoefunctions_obj.human_move(board, human)
            board[move] = human
        else:
            move = tictactoefunctions_obj.computer_move(board, computer, human)
            board[move] = computer
        tictactoefunctions_obj.display_board(board)
        turn = tictactoefunctions_obj.next_turn(turn)

    the_winner = tictactoefunctions_obj.winner(board)
    tictactoefunctions_obj.congrat_winner(the_winner, computer, human)



