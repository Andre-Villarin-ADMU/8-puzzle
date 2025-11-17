import random
import math
from collections import deque
import time

rows, cols = (3,3)
BLANK = " "
ELEMENTS = [BLANK, 1, 2, 3, 4, 5, 6, 7, 8]
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, BLANK)
HEADER_1 = "8 Puzzle - Breadth First Search (BFS) Algorithm"
BORDER = "=" * len(HEADER_1)
HEADER = [BORDER, HEADER_1]
NUM_ELEMENTS_TO_SELECT = 9
MOVE_OFFSETS = {
    "up": -3,
    "down": 3,
    "left": -1,
    "right": 1
}

def random_selector(elements, num_elements_to_select) -> tuple:
    '''
    Randomly chooses from ELEMENTS
    and determines the order in which
    these are added to a tuple state.
    '''
    state = []

    while (num_elements_to_select > 0):
        selected = random.choice(elements)
        elements.pop(elements.index(selected))
        state.append(selected)
        num_elements_to_select -= 1

    return tuple(state)

def arr_builder(raw_arr: list) -> list:
    '''
    Takes a 1D list 'raw_arr' and builds
    a nested list to create the
    grid layout.
    '''
    row_0 = raw_arr[0:3]
    row_1 = raw_arr[3:6]
    row_2 = raw_arr[6:]    
        
    built_arr = [row_0, row_1, row_2]

    return built_arr

def ui_helper(my_arr: list, is_BFS: bool, iter_number: int) -> str:
    '''
    This helper method references a list
    object 'my_arr' for printing out a minimal
    GUI in the console.
    '''
    if is_BFS: count_label = "(BFS) Depth #: "
    else: count_label = "(Non-BFS) Turn #: " 
    str_arr = f"{HEADER[0]}\n{HEADER[1]}\n{count_label}{iter_number}\n{HEADER[0]}\n\n"

    for i in range(len(my_arr)):
        for j in range (len(my_arr[i])):
            str_arr += f"[ {my_arr[i][j]} ]"
        str_arr += f"\n"
        
    return str_arr

def get_moves(index_to_move: int) -> list:
    try:
        row = index_to_move // 3
        col = index_to_move % 3
        valid_moves = []
        if (row > 0): 
            valid_moves.append("up")
        if (row < 2): 
            valid_moves.append("down")
        if (col > 0): 
            valid_moves.append("left")
        if (col < 2): 
            valid_moves.append("right")

        return valid_moves
    
    except ValueError:
        pass

def is_goal_state(my_arr: tuple) -> bool:
    return GOAL_STATE == my_arr

def move_tile(my_arr: list, valid_moves, selected_move: str) -> list:
    new_arr = my_arr.copy()
    try:
        offset = MOVE_OFFSETS[selected_move]
        new_arr[index] = new_arr[index + offset]
        new_arr[index + offset] = BLANK

    except:
        pass

    return new_arr

def find_neighbors(current_state: tuple) -> tuple:
    index = current_state.index(BLANK)
    valid_moves = get_moves(index)
    neighbor_result = []
    for move in valid_moves:
        new_state = list(current_state)
        new_state[index] = new_state[index + MOVE_OFFSETS[move]]
        new_state[index + MOVE_OFFSETS[move]] = BLANK
        neighbor_result.append((tuple(new_state), move))
    
    return neighbor_result

def get_path(parent: dict, moves: dict, goal_state: tuple) -> list:
    path = []
    move_arr = []
    state = goal_state

    while state is not None:
        path.append(state)
        move_arr.append(moves[state])
        state = parent[state]
    
    path.reverse()
    move_arr.reverse()

    return path, move_arr

def print_solution(path, move_arr):
    for i, state in enumerate(path):
        if i == 0:
            print("Start: ")
        else:
            print(f"Move {i}: {move_arr[i]}")
        current_state = arr_builder(list(state))
        print(ui_helper(current_state, False, i))

def bfs(init_state: tuple):
    root_node = init_state
    parent = {root_node: None}
    moves = {root_node: None}
    visited = {root_node: True}
    bfs_queue = deque([root_node])
    iter = 0

    while len(bfs_queue) > 0:
        current_state = bfs_queue.popleft()

        if is_goal_state(current_state):
            print(f"Solution found at iteration {iter+1}!")
            path, move_arr = get_path(parent, moves, current_state)
            print_solution(path, move_arr)
            return path, move_arr
        
        for new_state, move in find_neighbors(current_state):
            if new_state not in visited:
                visited[new_state] = True
                moves[new_state] = move
                parent[new_state] = current_state
                bfs_queue.append(new_state)
        iter += 1
    
    print("No solution exists. Start state may be of odd parity.")
    return None


# will clean up the code
is_BFS = True
state = random_selector(ELEMENTS, NUM_ELEMENTS_TO_SELECT)
formatted_list = arr_builder(list(state))
print(ui_helper(formatted_list, is_BFS, 0))

mode = input(("Use BFS? (Y/N): "))
if mode == "N": is_BFS = False

if is_BFS:
    bfs(state)
else:
    num_turns = 1
    while not is_goal_state(state):
        index = state.index(BLANK)
        valid_moves = get_moves(index)
        move = input(f"Move blank to? ({valid_moves}): ")
        unformatted_list = move_tile(list(state), valid_moves, move)
        formatted_list = arr_builder(unformatted_list)
        state = tuple(unformatted_list)
        print(ui_helper(formatted_list, is_BFS, num_turns))
        num_turns += 1
    print(f"Completed in {num_turns} moves")