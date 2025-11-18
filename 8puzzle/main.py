# This file contains the main function for the 8 puzzle problem

from puzzle import print_puzzle, is_solvable 
from dl_dfs import dl_dfs

def main():
    # Input initial state
    initial_state = input("Enter the initial state of the puzzle (e.g. 1 2 3 4 5 6 7 8 0): ")
    initial_state = [int(x) for x in initial_state.split()]
    print("Initial state:")
    iter_count = 0
    print_puzzle(initial_state, iter_count)

    # Input depth limit
    limit = int(input("Enter the depth limit for the depth limited DFS: "))

    if not is_solvable(initial_state):
        print("The puzzle is not solvable.")
    
    solution = dl_dfs(initial_state, limit)

    if solution:
        print("Solution found!")
        print("Depth of solution", len(solution) - 1)
        print("Solution path: ")
        for state in solution:
            print_puzzle(state, iter_count)
            iter_count += 1

    else:
        print("\nNo solution found within the depth limit.\n")

if __name__ == "__main__":
    main()


