# Table of Contents
- [Overview](#Overview)
- [Contributors](##Contributors)
- [Features](##Features)
- [Project Files](#Project-Files)
- [Running the 8-Puzzle Solver](#Running-the-8-Puzzle-Solver)
- [Example](##Sample-Output)
- [Directory](#Links)

# Overview
This project demonstrates two search algorithms, namely **Breadth-First Search (BFS)** and **Depth-Limited Depth-First Search (DL-DFS)** by finding the solution path of an 8-puzzle configuration, if it exists.

This was developed for the completion of the **CSCI 111 - Introduction to AI course at the Ateneo de Manila University**.

## Contributors
Go, Jasper; Predigua, Dave; Villarin, Andre

## Features
- Allows user to select whether to generate a random 8-puzzle configuration, or create a custom configuration.
- Implements BFS and DL-DFS in finding the solution path.
- Determines if a solution exists by ensuring the initial state is of even parity.
- Console-based UI: Displays the execution time, solution path, moves, and solution depth.

# Project Files
    8-puzzle/
    |
    |-- bfs.py      # contains BFS logic
    |-- dl_dfs.py   # contains DL-DFS logic
    |-- main.py     # implements console-based UI and input handling
    |-- puzzle.py   # contains main logic and other helper methods used by bfs and dl_dfs
    |-- README.md

# Running the 8-Puzzle Solver

1. Download .zip file from GDrive or GitHub Repository

    if using git:
        `git clone https://github.com/Andre-Villarin-ADMU/8-puzzle.git`

    then:
        `cd <directory of files>`

2. Run main.py (req: python)

        python3 main.py

3. Follow prompts displayed by the console

## Sample Output

    Try: 8 3 6 0 1 5 4 2 7
    
    --- Initial State ---
    [8] [3] [6]
    [ ] [1] [5]
    [4] [2] [7]

Choose Algorithm: Breadth-First Search (B) or Depth-Limited DFS (D)? (B/D): B

    Solution found at iteration 77441! Time taken: 0.0910 seconds

    Step 21 (right):
    [1] [2] [3]
    [4] [5] [6]
    [7] [8] [ ]

    Total Moves: 21

Choose Algorithm: Breadth-First Search (B) or Depth-Limited DFS (D)? (B/D): D
Enter the Depth Limit (e.g., 20): 30

    Solution found within depth limit 30! Time taken: 0.1472 seconds

    Step 29 (down):
    [1] [2] [3]
    [4] [5] [6]
    [7] [8] [ ]

    Total Moves: 29

# Links
Google Drive: https://drive.google.com/drive/folders/1fxiWanhE19Bb7-JkZ0G1Ne7TV4QSE4eP?usp=drive_link
