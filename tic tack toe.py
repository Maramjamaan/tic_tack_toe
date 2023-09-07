import numpy as np

# Initialize the game board
board = np.full((3, 3), ' ')

def print_board():
    print(board)

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]


    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # Check if the board is full
    if ' ' not in board:
        return 'Draw'

    # The game is not over yet
    return None

def get_move(player):
    while True:
        move = input(f"Player {player}, enter your move (row[0-2] col[0-2]): ")
        row, col = map(int, move.split())
        if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == ' ':
            return row, col

def play_game():
    player = 'X'
    while True:
        print_board()
        row, col = get_move(player)
        board[row][col] = player

        winner = check_winner()
        if winner:
            print_board()
            if winner == 'Draw':
                print("It's a Draw!")
            else:
                print(f"Player {winner} wins!")
            break

        player = 'O' if player == 'X' else 'X'


play_game()

