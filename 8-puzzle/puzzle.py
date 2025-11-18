import random
from bfs import *

HEADER_1 = "8 Puzzle - Breadth First Search (BFS) Algorithm"
BORDER = "=" * len(HEADER_1)
HEADER = [BORDER, HEADER_1]
NUM_ELEMENTS_TO_SELECT = 9
BLANK = 0

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

def game_loop(state: tuple, num_turns: int) -> tuple:
    index = state.index(BLANK)
    valid_moves = get_moves(index)
    move = input(f"Move blank to? ({valid_moves}): ")
    unformatted_list = move_tile(list(state), valid_moves, move)
    formatted_list = arr_builder(unformatted_list)
    state = tuple(unformatted_list)
    print(ui_helper(formatted_list, False, num_turns))
    return state