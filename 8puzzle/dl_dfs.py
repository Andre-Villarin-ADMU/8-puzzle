# This file contains the depth limited depth first search algorithm for the 8 puzzle problem

from puzzle import get_moves

def dl_dfs(state, limit, goal=[1,2,3,4,5,6,7,8,0]):
    '''
    Initializes the search, handles list/tuple conversion for optimization, and converts the final path back to lists.
    '''
    # Convert input list states to  tuples for efficient hashing
    initial_tuple = tuple(state)
    goal_tuple = tuple(goal)

    # Path starts as a list of tuples
    solution_path = recursive_dfs(initial_tuple, goal_tuple, limit, path=[initial_tuple])

    if solution_path:
        # Convert path back to a list for display
        return [list(s) for s in solution_path]
    
    return None

def recursive_dfs(state, goal, limit, path):
    # If the goal state is reached, return the solution path
    if state == goal:
        return path
    # If the depth limit is reached, return a cutoff message
    if limit == 0:
        return None

    # Create a set from current path list
    path_set = set(path)
    
    # Else, explore all possible moves
    # Convert state tuple back to list
    for move_list in get_moves(list(state)):
        move_tuple = tuple(move_list)
        
        # If the move is not in the path yet, add it and continue the search
        if move not in path:
            result = recursive_dfs(move_tuple, goal, limit-1, path+[move_tuple])
            # If it finds a solution, return the solution path
            if result is not None:
                return result

    return None
