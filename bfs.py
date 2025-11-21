# bfs.py

from collections import deque
import time
from puzzle import is_solvable, is_goal_state, get_neighbors, get_path, print_solution

def bfs(init_state: tuple):
    '''
    Implements the Breadth-First Search algorithm for the 8-puzzle.
    '''
    start = time.perf_counter()
    
    if not is_solvable(init_state):
        print("No solution exists. Start state is of odd parity.")
        return None

    # Data Structures for BFS
    root_node = init_state
    parent = {root_node: None} # Tracks the state from which the current state was reached
    moves = {root_node: None}  # Tracks the move (up/down/etc.) used to reach the state
    visited = {root_node}      # Tracks all states already explored
    bfs_queue = deque([root_node])
    iterations = 0

    while bfs_queue:
        current_state = bfs_queue.popleft()
        iterations += 1

        if is_goal_state(current_state):
            end = time.perf_counter()
            print(f"Solution found at iteration {iterations}! Time taken: {end - start:.4f} seconds")
            path, move_arr = get_path(parent, moves, current_state)
            print_solution(path, move_arr, "BFS")
            return path
        
        for new_state, move in get_neighbors(current_state):
            if new_state not in visited:
                visited.add(new_state)
                moves[new_state] = move
                parent[new_state] = current_state
                bfs_queue.append(new_state)
    
    # Should not be reached if the puzzle is solvable and GOAL_STATE is correct
    print("Search failed (This should only happen if puzzle is unsolvable or goal state is unreachable).")
    return None