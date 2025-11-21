# main.py

from puzzle import random_selector, ELEMENTS, is_solvable, format_puzzle
from bfs import bfs
from dl_dfs import dl_dfs

def get_initial_state():
    mode = input("Generate a random solvable state (R) or enter a custom state (C)? (R/C): ").upper()
    
    if mode == 'C':
        while True:
            try:
                # Expecting space-separated numbers, e.g., "1 2 3 4 5 6 7 8 0"
                state_str = input("Enter the 9 tile numbers (1-8 and 0 for blank, separated by spaces): ")
                state = tuple(int(x) for x in state_str.split())
                
                if len(state) != 9 or sorted(list(state)) != sorted(ELEMENTS):
                    print("Invalid input. Must be 9 unique numbers (0-8).")
                    continue
                
                if not is_solvable(state):
                    print("This state is NOT solvable. Please enter a solvable state or try another one.")
                    continue
                
                return state
            except ValueError:
                print("Invalid input. Please use numbers only.")
    else:
        # Keep generating random states until a solvable one is found
        while True:
            state = random_selector(ELEMENTS)
            if is_solvable(state):
                print("Generated a random solvable state.")
                return state

def main():
    print("=" * 30)
    print("      8 Puzzle Solver      ")
    print("=" * 30)
    
    # 1. Get Initial State
    init_state = get_initial_state()
    print("\n--- Initial State ---")
    print(format_puzzle(init_state))
    
    # 2. Select Algorithm
    while True:
        algo_choice = input("Choose Algorithm: Breadth-First Search (B) or Depth-Limited DFS (D)? (B/D): ").upper()
        if algo_choice in ('B', 'D'):
            break
        print("Invalid choice. Please enter 'B' or 'D'.")
        
    # 3. Run Search
    if algo_choice == 'B':
        bfs(init_state)
    elif algo_choice == 'D':
        while True:
            try:
                limit = int(input("Enter the Depth Limit (e.g., 20): "))
                if limit > 0:
                    break
                print("Limit must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        dl_dfs(init_state, limit)

if __name__ == "__main__":
    main()