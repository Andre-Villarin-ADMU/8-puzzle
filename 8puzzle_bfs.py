import random
import math

rows, cols = (3,3)
ELEMENTS = [" ", 1, 2, 3, 4, 5, 6, 7, 8]
GOAL_STATE = [1, 2, 3, 8, " ", 4, 7, 6, 5]
HEADER_1 = "8 Puzzle - Breadth First Search (BFS) Algorithm"
BORDER = "=" * len(HEADER_1)
HEADER = [BORDER, HEADER_1]
NUM_ELEMENTS_TO_SELECT = 9
MOVE_OFFSETS = {
    "up": -3,
    "down": 3,
    "left": -1,
    "right": 1
}

def random_selector(elements, num_elements_to_select) -> list:
    '''
    Randomly chooses from ELEMENTS
    and determines the order in which
    these are added to a list raw_arr.
    '''
    raw_arr = []

    while (num_elements_to_select > 0):
        selected = random.choice(elements)
        elements.pop(elements.index(selected))
        raw_arr.append(selected)
        num_elements_to_select -= 1

    return raw_arr

def arr_builder(raw_arr) -> list:
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

def ui_helper(my_arr: list) -> str:
    '''
    This helper method references a list
    object 'my_arr' for printing out a minimal
    GUI in the console.
    '''
    str_arr = f"{HEADER[0]}\n{HEADER[1]}\n{HEADER[0]}\n\n"

    for i in range(len(my_arr)):
        for j in range (len(my_arr[i])):
            str_arr += f"[ {my_arr[i][j]} ]"
        str_arr += f"\n"
        
    return str_arr

def is_blank(my_arr: list, index_to_move: int, move: str):
    offset = MOVE_OFFSETS[move]
    to_check = my_arr[index_to_move + offset]
    return to_check == " "

def get_moves(my_arr, index_to_move: int) -> list:
    row = index_to_move // 3
    col = index_to_move % 3
    available_moves = []
    valid_moves = []
    if (row > 0): 
        available_moves.append("up")
    if (row < 2): 
        available_moves.append("down")
    if (col > 0): 
        available_moves.append("left")
    if (col < 2): 
        available_moves.append("right")

    for move in available_moves:
        print(move)
        if is_blank(my_arr, index_to_move, move):
            valid_moves.append(move)

    return valid_moves

def is_goal_state(my_arr) -> bool:
    return GOAL_STATE == my_arr
def move_tile(my_arr: list, tile):
    try:
        index = my_arr.index(int(tile))
        valid_moves = get_moves(my_arr, index)

        for move in valid_moves:
            offset = MOVE_OFFSETS[move]
            my_arr[index + offset] = my_arr[index]
            my_arr[index] = " "

    except ValueError:
        pass


# Some test code:
unformatted_list = random_selector(ELEMENTS, NUM_ELEMENTS_TO_SELECT)
formatted_list = arr_builder(unformatted_list)
print(ui_helper(formatted_list))

is_manual = True
mode = input(("Manual Mode (non-BFS)? (Enter Y/N): "))
if mode == "Y": is_manual
else: is_manual = False
if is_manual:
    num_turns = 0
    while not is_goal_state(unformatted_list):
        tile = input("What tile to move (enter a digit): ")
        move_tile(unformatted_list, tile)
        formatted_list = arr_builder(unformatted_list)
        print(ui_helper(formatted_list))
        num_turns += 1
    print(f"Completed in {num_turns} moves")

else:
    # bfs implementation
    pass