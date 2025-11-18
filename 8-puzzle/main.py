from bfs import *
from puzzle import *

def main():
    is_BFS = True
    # test_state = (8, 6, 7, 2, 5, 4, 3, BLANK, 1) # most difficult but solvable state
    # state = test_state
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
            state = game_loop(state, num_turns)
            num_turns += 1
        print(f"Completed in {num_turns} moves")

if __name__ == "__main__":
    main()