from collections import deque
import time

rows, cols = (3,3)
BLANK = 0
ELEMENTS = [BLANK, 1, 2, 3, 4, 5, 6, 7, 8]
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, BLANK)
MOVE_OFFSETS = {
    "up": -3,
    "down": 3,
    "left": -1,
    "right": 1
}

def is_solvable(my_arr: list):
    # Remove the blank index
    arr = [x for x in my_arr if x != 0]

    # Calculate the inversion count
    inv_count = 0
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1 
    # If the inversion count is odd, then the puzzle is not solvable
    
    return inv_count % 2 == 0
    # If the inversion count is even, then the puzzle is solvable

def is_goal_state(my_arr: tuple) -> bool:
    return GOAL_STATE == my_arr

def move_tile(my_arr: list, valid_moves, selected_move: str) -> list:
    new_arr = my_arr.copy()
    index = new_arr.index(BLANK)
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
        swap_index = index + MOVE_OFFSETS[move]
        new_state = list(current_state)
        new_state[index], new_state[swap_index] = new_state[swap_index], new_state[index]
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
    from puzzle import arr_builder, ui_helper
    for i, state in enumerate(path):
        if i == 0:
            print("Start: ")
        else:
            print(f"Move {i}: {move_arr[i]}")
        current_state = arr_builder(list(state))
        print(ui_helper(current_state, True, i))

def bfs(init_state: tuple):
    start = time.perf_counter()
    root_node = init_state
    parent = {root_node: None}
    moves = {root_node: None}
    visited = {root_node: True}
    bfs_queue = deque([root_node])
    iter = 0

    if (not is_solvable(list(init_state))):
        print("No solution exists. Start state is of odd parity.")
        return None

    while len(bfs_queue) > 0:
        current_state = bfs_queue.popleft()

        if is_goal_state(current_state):
            end = time.perf_counter()
            print(f"Solution found at iteration {iter+1}! Time taken: {end - start}")
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