# pylint: disable=missing-docstring

def valid_rows(grid):
    for row in grid:
        if len(row) != len(set(row)):
            return False
    return True

def valid_columns(grid):
    for j in range(0, 9):
        col = []
        for i in range(0, 9):
            col.append(grid[i][j])
        if len(col) != len(set(col)):
            return False
    return True

def retrieve_every_third_element(lst, start_index):
    return lst[start_index::3]

def valid_boxes(grid):
    rows = [row[i:i+3] for row in grid for i in range(0, len(row), 3)]
    batches = [rows[i:i+9] for i in range(0, len(rows), 9)]
    for batch in batches:
        for start_index in range(0,3):
            numbers = retrieve_every_third_element(batch, start_index)
            flat_list = [num for sublist in numbers for num in sublist]
            if not len(flat_list) == len(set(flat_list)):
                return False
    return True

def sudoku_validator(grid):
    return valid_rows(grid) and valid_columns(grid) and valid_boxes(grid)
