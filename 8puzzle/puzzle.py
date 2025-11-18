# puzzle.py
# This python file contains the utility functions for representing the 8-puzzle
HEADER_1 = "8 Puzzle - Depth Limited DFS Algorithm"
BORDER = "=" * len(HEADER_1)
HEADER = [BORDER, HEADER_1]
BLANK = 0

'''
Print the puzzle in a 3x3 grid
'''
def print_puzzle(puzzle, iter_count: int):
    count_label = "(Depth-Limited DFS) Depth #: "
    nested_arr = [puzzle[0:3], puzzle[3:6], puzzle[6:]]
    str_arr = f"{HEADER[0]}\n{HEADER[1]}\n{count_label}{iter_count}\n{HEADER[0]}\n\n"

    for i in range(len(nested_arr)):
        for j in range (len(nested_arr[i])):
            str_arr += f"[ {nested_arr[i][j]} ]"
        str_arr += f"\n"
    
    print(str_arr)

'''
Return a list of all possible moves from the current state
'''
def get_moves(puzzle):
    moves = []
    zero_index = puzzle.index(0) # position of the blank space
    row, col = divmod(zero_index, 3) # row and column of the blank space

    # Directions that the blank space can move
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(puzzle)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]

            moves.append(new_state)

    return moves

'''
Check if the puzzle can be solved
'''
def is_solvable(puzzle):
    # Remove the blank index
    arr = [x for x in puzzle if x != 0]

    # Calculate the inversion count
    inv_count = 0
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1 
    # If the inversion count is odd, then the puzzle is not solvable
    
    return inv_count % 2 == 0
    # If the inversion count is even, then the puzzle is solvable





        