# Conways-Game-Of-Life 
An **in progress** attempt at Conways Game Of Life

## Information

Game of Life, is a cellular automation zero-player game. It starts with an initial configuration setup by the user, that initial setup is the only interaction with the game.

### Rules

Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occurs:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.

2. Any live cell with two or three live neighbours lives on to the next generation.

3. Any live cell with more than three live neighbours dies, as if by overpopulation.

4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Installation

### Dependencies

* Use ` pip install -r requirements.txt ` to install the required packages
