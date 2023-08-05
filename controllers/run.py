import random

# Constants
BOARD_SIZE = 5
NUM_BATTLESHIPS = 3
NUM_ATTEMPTS = 10

# Function to initialize the game board
def create_board():
    return [['O' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Function to place Battleships randomly on the board
def place_battleships(board):
    for _ in range(NUM_BATTLESHIPS):
        while True:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            if board[row][col] != 'B':
                board[row][col] = 'B'
                break


# Function to display the game board
def display_board(board):
    print("\n  ", end="")
    for col in range(BOARD_SIZE):
        print(col, end=" ")
    print()
    for row in range(BOARD_SIZE):
        print(row, end=" ")
        for col in range(BOARD_SIZE):
            print(board[row][col], end=" ")
        print()
    print()

# Function to check if the shot hit a Battleship
def check_shot(board, row, col):
    if board[row][col] == 'B':
        print("Hit!")
        board[row][col] = 'X'
        return True
    else:
        print("Miss!")
        return False
