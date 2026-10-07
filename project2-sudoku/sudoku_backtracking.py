import time

sudoku_puzzles = {
    "SUDOKU 1": [
        [0, 3, 4, 0, 0, 0, 6, 0, 0],
        [0, 0, 2, 6, 0, 0, 0, 8, 0],
        [0, 6, 8, 3, 0, 0, 0, 0, 7],
        [0, 0, 3, 0, 0, 1, 0, 0, 5],
        [0, 5, 9, 0, 6, 0, 0, 7, 2],
        [0, 0, 0, 5, 2, 0, 0, 4, 6],
        [2, 0, 5, 9, 0, 6, 0, 0, 0],
        [0, 0, 0, 4, 0, 8, 0, 5, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 4]
    ],
    "SUDOKU 2": [
        [0, 0, 0, 5, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 8, 9, 0, 2, 0],
        [7, 8, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 3, 4, 6, 0, 0, 8],
        [0, 4, 0, 2, 9, 0, 0, 5, 0],
        [8, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 7, 0, 4, 2],
        [4, 0, 0, 0, 6, 0, 8, 0, 5],
        [6, 0, 8, 0, 0, 5, 0, 3, 0]
    ],
    "SUDOKU 3": [
        [0, 4, 0, 0, 0, 0, 3, 0, 0],
        [0, 3, 6, 0, 7, 2, 0, 0, 0],
        [0, 7, 8, 0, 6, 0, 4, 0, 0],
        [0, 8, 3, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 5],
        [0, 2, 5, 0, 0, 8, 0, 7, 0],
        [3, 0, 0, 0, 0, 4, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 4, 0],
        [7, 6, 4, 0, 8, 9, 5, 3, 0]
    ],
    "SUDOKU 4": [
        [0, 0, 0, 0, 7, 4, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 6],
        [0, 7, 9, 0, 0, 0, 3, 0, 0],
        [6, 0, 0, 7, 2, 8, 0, 0, 9],
        [9, 8, 0, 5, 0, 3, 0, 0, 0],
        [0, 3, 7, 9, 4, 0, 0, 5, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 3, 0, 0, 6, 0],
        [0, 6, 0, 4, 9, 0, 0, 2, 3]
    ],
    "SUDOKU 5": [
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 9, 8, 0, 7, 0, 6, 0, 0],
        [2, 0, 0, 0, 0, 0, 7, 5, 9],
        [0, 0, 0, 0, 8, 0, 9, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 4, 1],
        [9, 0, 7, 0, 0, 3, 0, 0, 5],
        [1, 6, 9, 0, 0, 0, 4, 0, 0],
        [0, 0, 3, 4, 0, 1, 0, 9, 0],
        [7, 5, 0, 8, 0, 9, 0, 3, 0]
    ],
    "SUDOKU 6": [
        [0, 6, 0, 2, 0, 0, 0, 8, 0],
        [0, 8, 0, 6, 3, 4, 5, 0, 1],
        [0, 0, 0, 8, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 5, 6, 0, 8],
        [2, 4, 0, 3, 0, 0, 0, 5, 0],
        [0, 0, 0, 9, 6, 7, 0, 0, 2],
        [3, 0, 7, 0, 0, 0, 4, 0, 0],
        [0, 2, 5, 0, 4, 3, 0, 0, 7],
        [8, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    "SUDOKU 7": [
        [0, 8, 0, 6, 9, 3, 0, 0, 0],
        [0, 2, 0, 5, 0, 0, 0, 0, 4],
        [0, 7, 0, 0, 8, 4, 3, 5, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 3, 7, 8, 2, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 7],
        [0, 4, 0, 0, 0, 2, 0, 0, 6],
        [0, 5, 2, 7, 6, 0, 0, 0, 0]
    ],
    "SUDOKU 8": [
        [6, 0, 7, 0, 0, 5, 0, 1, 4],
        [5, 3, 9, 1, 0, 4, 2, 7, 0],
        [0, 2, 0, 0, 8, 7, 9, 6, 0],
        [9, 1, 8, 0, 0, 6, 0, 0, 7],
        [0, 0, 0, 7, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 7, 1, 5, 0, 0, 0, 8, 0],
        [2, 9, 0, 4, 0, 8, 0, 0, 0],
        [8, 0, 0, 6, 0, 2, 0, 4, 9]
    ],
    "SUDOKU 9": [
        [0, 0, 7, 0, 0, 1, 0, 0, 4],
        [1, 3, 0, 0, 5, 0, 8, 6, 0],
        [0, 0, 5, 0, 0, 4, 0, 0, 0],
        [6, 0, 8, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 9, 0, 3],
        [0, 0, 0, 9, 0, 0, 1, 0, 0],
        [0, 7, 2, 0, 8, 0, 0, 9, 5],
        [5, 0, 0, 7, 0, 0, 4, 0, 0]
    ],
    "SUDOKU 10": [
        [0, 2, 6, 0, 3, 0, 4, 7, 0],
        [0, 0, 0, 2, 0, 0, 5, 1, 0],
        [7, 0, 0, 9, 0, 0, 0, 2, 0],
        [5, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 7],
        [0, 8, 0, 0, 0, 9, 0, 0, 1],
        [0, 3, 4, 0, 0, 6, 0, 0, 0],
        [0, 9, 5, 0, 7, 0, 6, 4, 0]
    ]
}

def is_valid(sudoku_grid, num, x, y):
    for i in range(9):
        if num == sudoku_grid[x][i] or num == sudoku_grid[i][y]: #checking if the number is in the same line or the same column
            return False

    xsquare = (x // 3) * 3
    ysquare = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku_grid[xsquare + i][ysquare + j] == num: #checking if the number is in the same 3x3 box
                return False
    return True

def blank(sudoku_grid):

    empty_positions = []
    for a in range(9):
        for b in range(9):
            if sudoku_grid[a][b] == 0:  
                empty_positions.append((a, b))
    return empty_positions

def SudoBT(sudoku_grid, indx, empty_positions=None):
    if empty_positions == None: #base case
        empty_positions = blank(sudoku_grid)

    if indx == len(empty_positions): #if we filled every empty position  
        return True  

    x, y = empty_positions[indx]  #current empty position

    for num in range(1, 10):  #for every number
        if is_valid(sudoku_grid, num, x, y): #if we can put it in the current empty position
            sudoku_grid[x][y] = num  

            if SudoBT(sudoku_grid, indx + 1, empty_positions):
                return True  

            sudoku_grid[x][y] = 0  #we undo what we did cause there is no solution with the number we chose this iteration

    return False  #if after all the itertion, no number works, must be an insolvable sudoku


# sudoku printing function 
def print_sdk(grid):
    for row in grid:
        print(row)
    print("")

start = time.time()

# tests
if SudoBT(sudoku_puzzles["SUDOKU 1"], 0): 
    print("SUDOKU 1")
    print_sdk(sudoku_puzzles['SUDOKU 1'])

if SudoBT(sudoku_puzzles["SUDOKU 2"], 0): 
    print("SUDOKU 2")
    print_sdk(sudoku_puzzles['SUDOKU 2'])

if SudoBT(sudoku_puzzles["SUDOKU 3"], 0): 
    print("SUDOKU 3")
    print_sdk(sudoku_puzzles['SUDOKU 3'])

if SudoBT(sudoku_puzzles["SUDOKU 4"], 0): 
    print("SUDOKU 4")
    print_sdk(sudoku_puzzles['SUDOKU 4'])

if SudoBT(sudoku_puzzles["SUDOKU 5"], 0): 
    print("SUDOKU 5")
    print_sdk(sudoku_puzzles['SUDOKU 5'])

if SudoBT(sudoku_puzzles["SUDOKU 6"], 0): 
    print("SUDOKU 6")
    print_sdk(sudoku_puzzles['SUDOKU 6'])

if SudoBT(sudoku_puzzles["SUDOKU 7"], 0): 
    print("SUDOKU 7")
    print_sdk(sudoku_puzzles['SUDOKU 7'])

if SudoBT(sudoku_puzzles["SUDOKU 8"], 0): 
    print("SUDOKU 8")
    print_sdk(sudoku_puzzles['SUDOKU 8'])

if SudoBT(sudoku_puzzles["SUDOKU 9"], 0): 
    print("SUDOKU 9")
    print_sdk(sudoku_puzzles['SUDOKU 9'])

if SudoBT(sudoku_puzzles["SUDOKU 10"], 0): 
    print("SUDOKU 10")
    print_sdk(sudoku_puzzles['SUDOKU 10'])
    
end = time.time()

time_algo = end-start
print(f"The time is {time_algo:.4f} sec")

