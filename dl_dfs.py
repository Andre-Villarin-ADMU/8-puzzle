# dl_dfs.py

import time
from puzzle import is_solvable, is_goal_state, get_neighbors, get_path, print_solution

def recursive_dfs(state, goal, limit, path, parent, moves):
    '''
    Recursive helper function for DL-DFS.
    Returns: goal_state_tuple if solution found, else None
    '''
    if is_goal_state(state):
        return state
    
    # If the depth limit is reached, stop searching along this path
    if limit == 0:
        return None
    
    # Explore all possible neighbors
    for next_state, move in get_neighbors(state):
        
        # Check if the next state is not already in the current path 
        # (This is important for DFS to avoid immediate cycles and repeated states on the path)
        if next_state not in path:
            # Update parent/moves for path reconstruction upon success
            parent[next_state] = state
            moves[next_state] = move

            # Recurse with reduced limit and extended path
            result = recursive_dfs(next_state, goal, limit - 1, path + (next_state,), parent, moves)
            
            # If a solution is found in the recursive call, pass it up
            if result is not None:
                return result

    return None

def dl_dfs(init_state: tuple, limit: int):
    '''
    Implements the Depth-Limited Depth-First Search algorithm.
    '''
    start = time.perf_counter()

    if not is_solvable(init_state):
        print("No solution exists. Start state is of odd parity.")
        return None
    
    # DL-DFS uses a path check instead of a global visited set.
    # We pass parent/moves dictionaries to the recursive function to track the solution path.
    parent = {init_state: None}
    moves = {init_state: None}

    # Start the recursive search
    goal_state_found = recursive_dfs(init_state, limit, limit, (init_state,), parent, moves)

    if goal_state_found:
        end = time.perf_counter()
        print(f"Solution found within depth limit {limit}! Time taken: {end - start:.4f} seconds")
        path, move_arr = get_path(parent, moves, goal_state_found)
        print_solution(path, move_arr, f"DL-DFS (Limit={limit})")
        return path
    else:
        end = time.perf_counter()
        print(f"\nNo solution found within the depth limit of {limit}. Time taken: {end - start:.4f} seconds\n")
        return None