README = """
# Battleship Game in Python

A simple text-based Battleship game implemented in Python.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Game Features](#game-features)
- [Screenshots](#screenshots)
- [Code Structure](#code-structure)
- [Known Issues and Limitations](#known-issues-and-limitations)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Credits](#credits)

## Installation

1. Clone the repository: git clone https://github.com/vendelaswenson/portfolio3.git
2. Change into the project directory: cd portfolio3
3. Run the game: python3 run.py

## Usage

1. The game board will be displayed, and you will be prompted to enter row and column coordinates to fire at a cell on the board.
2. Follow the instructions on the screen to guess the location of the hidden battleships and try to sink them all.
3. You have a limited number of attempts to complete the game.

## Game Features

- Randomly placed battleships on the game board.
- Simple and intuitive text-based interface.
- Limited number of attempts to keep the game challenging.

## Screenshots
[Link Text](./views/battleship.pdf)


## Code Structure

The code is organized into several functions to handle different aspects of the game.

- `create_board()`: Initializes the game board with empty cells.
- `place_battleships(board)`: Randomly places the battleships on the board.
- `display_board(board)`: Displays the game board to the player.
- `check_shot(board, row, col)`: Checks if the player's shot hits a battleship.
- `play_game()`: Main game loop to run the game.

## Known Issues and Limitations

- The game does not support customization of board size or number of battleships at this time.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, you can reach out to the project maintainer at vendelaswenson@outlook.com.

## Credits

- The Battleship game idea and rules were inspired by the classic Battleship board game.
- Special thanks to the Python community and contributors for their support.
"""


