import random

board = [i for i in range (9)]

def print_board(board):
    print("   |   |   ")
    print(" " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print("---|---|---")
    print(" " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print("---|---|---")
    print(" " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))
    print("   |   |   ")
    
def check_board(board):
    return all(isinstance(b, str) for b in board)

def player_input(pos, board):
    if isinstance(board[pos], str):
        print("Posisi telah diambil")
        return False
    else:
        board[pos] = "X"
        return True

def computer_input(board):
    empty_board = []
    for i in range(0,9):
        if not isinstance(board[i], str):
            empty_board.append(board[i])
    board[random.choice(empty_board)] = "O"

def check_win(board, sym):
    for i in range(0,9):
        if i == 0 or i == 3 or i == 6:
            if board[i] == board[i+1] == board[i+2] == sym:
                return True
        if i == 0 or i == 1 or i == 2:
            if board[i] == board[i+3] == board[i+6] == sym:
                return True
        if i == 0:
            if board[i] == board[i+4] == board[i+8] == sym:
                return True
        if i == 2:
            if board[i] == board[i+2] == board[i+4] == sym:
                return True

print("Tic Tac Toe")

while not check_board(board):
    print_board(board)
    pos = int(input("Masukkan posisi: "))
    
    if player_input(pos, board):
        if check_win(board, "X"):
            break

        computer_input(board)
        if check_win(board, "O"):
            break

print_board(board)
if check_win(board, "X"):
    print("Anda Menang!")
elif check_win(board, "O"):
    print("Anda Kalah!")
else:
    print("Seri!")

    

