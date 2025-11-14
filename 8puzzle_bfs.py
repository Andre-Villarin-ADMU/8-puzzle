import random
import math

rows, cols = (3,3)
ELEMENTS = [0, 1, 2, 3, 4, 5, 6, 7, 8]
HEADER_1 = "8 Puzzle - <Insert Algorithm Name>"
BORDER = "=" * len(HEADER_1)
HEADER = [BORDER, HEADER_1]
NUM_ELEMENTS_TO_SELECT = 8


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
    row_0 = [" ", " ", " "]
    row_1 = [" ", " ", " "]
    row_2 = [" ", " ", " "]

    for i in range(len(raw_arr)):
        element_to_add = raw_arr[i]
        row = math.floor(raw_arr[i] / 3)
        col = raw_arr[i] % 3

        if row == 0:
            row_0[col] = element_to_add

        elif row == 1:
            row_1[col] = element_to_add

        else:
            row_2[col] = element_to_add
        
    built_arr = [row_0, row_1, row_2]

    return built_arr

def ui_helper(my_arr: list):
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

# Some test code:
unformatted_list = random_selector(ELEMENTS, NUM_ELEMENTS_TO_SELECT)
formatted_list = arr_builder(unformatted_list)
print(ui_helper(formatted_list))
