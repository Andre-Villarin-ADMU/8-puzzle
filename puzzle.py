# puzzle.py

import random

# Constants
ROWS, COLS = (3, 3)
BLANK = 0
ELEMENTS = [BLANK, 1, 2, 3, 4, 5, 6, 7, 8]
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, BLANK)
MOVE_OFFSETS = {
    "up": -3,
    "down": 3,
    "left": -1,
    "right": 1
}
HEADER_1 = "8 Puzzle Solver"
BORDER = "=" * len(HEADER_1)

def random_selector(elements: list, num_elements_to_select: int = 9) -> tuple:
    '''
    Randomly chooses elements and determines the initial state tuple.
    '''
    state_list = []
    
    # Create a mutable copy
    available_elements = elements.copy()

    while (num_elements_to_select > 0):
        selected = random.choice(available_elements)
        available_elements.remove(selected)
        state_list.append(selected)
        num_elements_to_select -= 1

    return tuple(state_list)

def is_solvable(state: tuple) -> bool:
    '''
    Checks if the puzzle state is solvable based on the inversion count.
    '''
    # Remove the blank tile
    arr = [x for x in state if x != BLANK]

    # Calculate the inversion count
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1 
    
    # For a 3x3 grid, solvability requires an even inversion count
    return inv_count % 2 == 0

def is_goal_state(state: tuple) -> bool:
    
    # Checks if the current state matches the goal state.
    return GOAL_STATE == state

def get_neighbors(current_state: tuple) -> list[tuple]:
    '''
    Generates all valid neighbor states and the move (direction) required to reach them.
    Returns: [(new_state, move_direction), ...]
    '''
    index = current_state.index(BLANK)
    row = index // COLS
    col = index % COLS
    
    # Determine which moves are valid based on the blank's position
    valid_moves = []
    if row > 0: valid_moves.append("up")
    if row < ROWS - 1: valid_moves.append("down")
    if col > 0: valid_moves.append("left")
    if col < COLS - 1: valid_moves.append("right")

    neighbor_results = []
    for move in valid_moves:
        swap_index = index + MOVE_OFFSETS[move]
        
        # Create a new state list from the tuple
        new_state_list = list(current_state)
        
        # Swap the blank tile with the adjacent tile
        new_state_list[index], new_state_list[swap_index] = new_state_list[swap_index], new_state_list[index]
        
        neighbor_results.append((tuple(new_state_list), move))
    
    return neighbor_results

def get_path(parent: dict, moves: dict, goal_state: tuple) -> tuple[list, list]:
    '''
    Reconstructs the solution path and move sequence from the parent/moves dictionaries.
    '''
    path = []
    move_arr = []
    state = goal_state

    # Trace back from the goal state to the root (parent=None)
    while state is not None:
        path.append(state)
        move_arr.append(moves.get(state)) # Use .get for root state (None)
        state = parent.get(state)
    
    path.reverse()
    move_arr.reverse()

    return path, move_arr

def format_puzzle(state: tuple) -> str:
    '''
    Formats the 1D state tuple into a readable 3x3 grid string.
    '''
    grid_str = ""
    for i in range(0, len(state), COLS):
        row = state[i:i + COLS]
        row_str = " ".join(f"[{' ' if tile == BLANK else tile}]" for tile in row)
        grid_str += row_str + "\n"
    return grid_str

def print_solution(path: list, move_arr: list, algorithm: str):
    '''
    Prints the step-by-step solution path.
    '''
    print(f"\n--- Solution Path ({algorithm}) ---")
    for i, state in enumerate(path):
        current_move = move_arr[i] if i > 0 else "Start"
        print(f"\nStep {i} ({current_move}):")
        print(format_puzzle(state))
    print(f"Total Moves: {len(path) - 1}")