import copy

sudoku = [
		[3, 5, 0, 6, 0, 2, 0, 0, 4],
		[0, 0, 7, 0, 4, 0, 0, 1, 3],
		[0, 6, 9, 8, 3, 1, 0, 0, 7],
		[5, 0, 3, 0, 0, 0, 0, 9, 6],
		[0, 0, 0, 3, 0, 0, 7, 4, 5],
		[9, 4, 6, 0, 0, 0, 8, 0, 0],
		[6, 9, 2, 4, 0, 0, 0, 0, 8],
		[8, 0, 0, 7, 0, 3, 0, 0, 0],
		[0, 0, 4, 0, 2, 0, 0, 0, 1],
	]

operative_sudoku = copy.deepcopy(sudoku)


def sudoku_solver(row, col, direction):
    
    # Return completed board
    if row == 8 and col == 8 and sudoku[row][col] != 0 or is_valid(operative_sudoku[row][col], row, col):
        return operative_sudoku

    # Navigate past static positions
    if sudoku[row][col] != 0:
        if col == 8 and direction == 1:
            return sudoku_solver(row + direction, 0, direction)
        elif col == 0 and direction == -1:
            return sudoku_solver(row + direction, 8, direction)
        else:
            return sudoku_solver(row, col + direction, direction)
    
    # Find a valid n
    n = operative_sudoku[row][col]
    if is_valid(n, row, col) == False:
        while is_valid(n, row, col) == False:
            n += 1
            if n == 10:
                n = 0
                break
    
    # Forwarding mechanism
    if is_valid(n, row, col):
        operative_sudoku[row][col] = n
        if col == 8:
            return sudoku_solver(row + 1, 0, 1)
        else:
            return sudoku_solver(row, col + 1, 1)

    # Backtracking mechanism
    if n == 0 and (row != 0 and col !=0):
        operative_sudoku[row][col] = n
        if col == 0:
            return sudoku_solver(row -1, 8, -1)
        else:
            return sudoku_solver(row, col -1, -1)


def is_valid(n, row, col):

    # Determines if n is valid at a given position
    row_list = operative_sudoku[row]
    col_list = [x[col] for x in operative_sudoku]
    box_list = []
    
    start_row = row - row % 3
    start_col = col - col % 3
    for x in range(3):
        for y in range(3):
            box_list.append(operative_sudoku[x + start_row][y + start_col])

    if n in row_list or n in col_list or n in box_list or n == 0:
        return False
    else:
        return True

 # Start row, start col, direction
solved = sudoku_solver(0, 0, 1)

print(solved)