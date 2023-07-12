# pylint: disable=missing-docstring
"""Constraint-model-based algorithm with backtracking"""
#from binhex import FInfo

LEN_GRID = 9

def find_empty(grid):
    for i in range(LEN_GRID):
        for j in range(LEN_GRID):
            if grid[i][j] == 0:
                return (i, j)
    return None

def valid(grid, number, position):
    # check row
    for i in range(LEN_GRID):
        if grid[position[0]][i] == number and position[1] != i:
            return False

    # check column
    for i in range(LEN_GRID):
        if grid[i][position[1]] == number and position[0] != i:
            return False

    # check square
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == number and (i, j) != position:
                return False

    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True

    row, col = find

    for i in range(1, 10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return grid

            grid[row][col] = 0

    return False

def print_grid(grid):
    for i in range(LEN_GRID):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(LEN_GRID):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

def sudoku_solver(grid):
    """Sudoku solver"""

    if not isinstance(grid, list):
        return 'invalid grid'

    for row in grid:
        if len(row) != LEN_GRID:
            return 'invalid grid'

    if len(grid) != LEN_GRID:
        return 'invalid grid'

    solve(grid)
    return grid

grid = [
    [7,0,0,  0,0,9,  0,0,0],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,0,  0,0,0],

    [0,0,0,  0,0,0,  4,0,0],
    [0,5,0,  0,4,6,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],

    [0,0,6,  0,0,0,  0,0,5],
    [2,0,0,  5,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,3,0]
]

print_grid(grid)
print(sudoku_solver(grid))
print_grid(grid)
