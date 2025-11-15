# This file contains the depth limited depth first search algorithm for the 8 puzzle problem

from puzzle import get_moves

def dl_dfs(state, goal, limit):
    '''
    This function implements the algorithm
    It returns either:
        1. A solution path
        2. A failure message
        3. A cutoff message
    '''
    return recursive_dfs(state, goal, limit, path=[])

def recursive_dfs(state, goal, limit, path):
    # If the goal state is reached, return the solution path
    if state == goal:
        return path
    # If the depth limit is reached, return a cutoff message
    if limit == 0:
        return 'cutoff'
    
    # Else, explore all possible moves
    for move in get_moves(state):
        # If the move is not in the path yet, add it and continue the search
        if move not in path:
            result = recursive_dfs(move, goal, limit-1, path+[move])
            
            # If it reach the limit, return the cutoff message
            if result == 'cutoff':
                return 'cutoff'
            # If it finds a solution, return the solution path
            elif result is not None:
                return result
