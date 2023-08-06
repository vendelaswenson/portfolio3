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


# Main game loop
def play_game():
    board = create_board()
    place_battleships(board)

    for attempt in range(1, NUM_ATTEMPTS + 1):
        display_board(board)
        try:
            row = int(input(f"Attempt {attempt}: Enter the row (0-{BOARD_SIZE-1}): "))
            col = int(input(f"Attempt {attempt}: Enter the column (0-{BOARD_SIZE-1}): "))
            if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter valid row and column coordinates.")
            continue

        if check_shot(board, row, col):
            if all(all(cell != 'B' for cell in row) for row in board):
                print("Congratulations! You sank all the Battleships!")
                break
        else:
            print("Try again!")

    else:
        print("Game Over! You ran out of attempts.")

        # Run the game
if __name__ == "__main__":
    play_game()

