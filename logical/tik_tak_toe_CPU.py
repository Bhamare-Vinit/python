import random

def print_board(board):
    # Print the Tic-Tac-Toe board
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    # Check if the board is full (draw)
    return all([cell != ' ' for row in board for cell in row])

def make_move(board, row, col, player):
    # Place player's mark on the board if the cell is empty
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def get_random_move(board):
    # Get a random empty cell for the computer's move
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else None

def play_game():
    # Initialize the board and set the current player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'O'  # Computer starts with 'O'

    while True:
        if current_player == 'O':
            # Computer's turn
            move = get_random_move(board)
            if move:
                row, col = move
                print(f"Computer chose cell: ({row + 1}, {col + 1})")
                make_move(board, row, col, current_player)
        else:
            # User's turn
            while True:
                try:
                    row, col = map(int, input("Enter row and column (1-3) separated by space: ").split())
                    row -= 1  # Adjust for 0-based index
                    col -= 1  # Adjust for 0-based index
                    if make_move(board, row, col, current_player):
                        break
                    else:
                        print("Cell already occupied! Try again.")
                except (ValueError, IndexError):
                    print("Invalid input! Enter numbers between 1 and 3.")

        # Print the board after each move
        print_board(board)

        # Check for a win or draw
        if is_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print("The game is a draw!")
            break

        # Switch player
        current_player = 'X' if current_player == 'O' else 'O'

# Start the game
play_game()
