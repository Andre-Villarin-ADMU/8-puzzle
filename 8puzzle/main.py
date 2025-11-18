# This file contains the main function for the 8 puzzle problem

from puzzle import print_puzzle, is_solvable, GOAL_STATE
from dl_dfs import dl_dfs

def display_solution(path_list: list, algo_name: str, limit: int):
    """
    Prints the puzzle states along the solution path.
    """
    if not path_list:
        print(f"\nNo solution found by {algo_name} within the limit of {limit}.")
        return

    print(f"\nSolution found by {algo_name} at depth {len(path_list_of_lists) - 1}!")
    
    for i, state_list in enumerate(path_list):
        move = "Start" if i == 0 else f"Move {i}"
        print(f"\n{move}")
        print_puzzle(state_list, algo_name, i)
        
def main():
   print("\n" + "="*50)
    print(" DL-DFS Search: ")
    
    dfs_state_list = [2, 8, 3, 1, 6, 4, 7, 0, 5] 
    
    if not is_solvable(dfs_state_list):
        print("Configuration is not solvable.")
        return

    dfs_limit = int(input("Enter the depth limit for DL-DFS: "))
    
    print_puzzle(dfs_state_list, "Initial Configuration", 0)

    # Execute DL-DFS
    dfs_path = dl_dfs_solve(dfs_state_list, dfs_limit)
    
    display_solution(dfs_path, "DL-DFS", dfs_limit)

if __name__ == "__main__":
    main()

