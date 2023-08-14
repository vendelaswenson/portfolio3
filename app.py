from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, static_url_path='/static')

# Create a 5x5 grid for the game (True for ships, False for empty)
grid = [[False for _ in range(5)] for _ in range(5)]

def generate_grid(rows, cols):
    grid = [[False for _ in range(cols)] for _ in range(rows)]

    # Place hidden elements (ships or targets) in random positions
    num_hidden_elements = rows * cols // 4  # Adjust this value as needed
    for _ in range(num_hidden_elements):
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        grid[row][col] = True

    return grid

def place_ships():
    # Place ships randomly on the grid
    for _ in range(3):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        grid[row][col] = True

def is_valid_guess(row, col):
    # Check if the guess is within the grid
    return 0 <= row < 5 and 0 <= col < 5

@app.route('/')
def index():
    return render_template('index.html', grid=grid)

@app.route('/guess', methods=['POST'])
def guess():
    row = int(request.form['row'])
    col = int(request.form['col'])

    if is_valid_guess(row, col):
        guess_result = grid[row][col]

        # Check if the guessed cell contains a ship (True) or is empty (False)
        if guess_result:
            response = {'hit': True}
        else:
            response = {'hit': False}
    else:
        response = {'error': 'Invalid guess'}

    return jsonify(response)


if __name__ == '__main__':
    generate_grid(rows=5, cols=5)  # Generate the grid once at the start
    place_ships()
    app.run()
