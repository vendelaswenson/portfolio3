README = """
# Battleship Game in Python

The Battleship game is a classic two-player strategy game that simulates naval warfare. Players engage in a thrilling battle of wits as they strategically deploy their fleet of ships and attempt to sink their opponent's ships before their own fleet is destroyed. The game offers a mix of luck and skill, requiring players to deduce the locations of their opponent's hidden ships while protecting their own.

* Purpose of the Game

The primary purpose of the Battleship game is to provide an engaging and competitive experience for players. It challenges their logical thinking, deduction skills, and decision-making abilities. Players must use strategy and intuition to make informed guesses about their opponent's ship placements while avoiding detection themselves. The game promotes critical thinking, spatial reasoning, and anticipation, making it an excellent source of entertainment that can be enjoyed by people of all ages.

* Key Functions and Mechanics

Ship Placement: Players begin by placing their ships on a grid, usually represented by rows and columns. The ships can be positioned vertically or horizontally, and their sizes may vary.

Guessing Opponent's Ships: Players take turns guessing the coordinates on the opponent's grid to target their ships. The opponent responds with "hit" or "miss," indicating whether the guessed location contains a ship.

Announcing Hits and Misses: When a player scores a hit, they get an additional turn to make another guess. If a player's guess is a miss, the turn goes to the opponent.

Winning Conditions: The game continues until one player's entire fleet is sunk. The player who sinks all of their opponent's ships first wins the game.

Hidden Grids: Each player has two grids: one for placing their ships (hidden from the opponent) and another to track their guesses about the opponent's fleet.

Strategy and Deduction: Players use a combination of logic and deduction to narrow down possible ship locations based on previous guesses and hits.

Variations and Adaptations: The game can be adapted for different settings and variations. For example, larger grids, additional ship types, and special abilities can add complexity and excitement to the gameplay.

Digital Versions: While the physical board game involves paper and pencil, digital versions of Battleship have become popular. These versions often include graphics, animations, and multiplayer options.

The Battleship game remains a timeless classic that has entertained generations of players. Its blend of tactical thinking, suspenseful gameplay, and the thrill of competition make it an enduring favorite in the world of strategy games. Whether played on paper or in digital format, Battleship continues to captivate players and challenge their strategic minds.

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

## Testing
I tested that the game works and you can get a hit and a miss
I tested that you can win
I tested so it doesn't work to put in invalid input

## Bugs
I had a problem getting the function play_game to work, I only got misses so I had to try different functions before it worked


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


