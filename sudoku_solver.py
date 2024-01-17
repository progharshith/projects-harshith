def findnextempty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) If none.)

    # keep in mind we are using 0-8 indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None  # if no spaces in the puzzle are empty

def is_valid(puzzle, guess, row, col):
    # returns True if valid, else False
    # let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # now the column
    col_vals = [puzzle[i][col] for i in range(9)]  # a bit of list comprehensions :)
    if guess in col_vals:
        return False

    # and then the square
    # iterate over the 3 values in the row/column
    row_start = (row // 3) * 3  # 1//3==0, 5//3==1, ...
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    # if none of these return false
    return True

def print_puzzle(puzzle): #a function that prints the sudoku puzzles in a readable way
    for i in range(9): #this is purely for visual sake. does not affect the functionality of any other functions
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(f"{puzzle[i][j]} ", end="")
        print()

def solve_sudoku(puzzle):
    # solving sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = findnextempty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True

    # step 2: if there's a place to put a number, then guess b/w 1 and 9
    for guess in range(1, 10):
        # step 3: check if valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # now recurse using this puzzle:
            # step 4: recursively call our function until we reach the end.
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid OR if our guess does not solve the puzzle
        # backtrack and try another number
        puzzle[row][col] = -1
    # step 6: if none of the numbers that we try work, then the puzzle is unsolvable

#now for a trial run:
if __name__ == "__main__":
    puzzle = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]
    ]

    print("Initial Puzzle:")
    print_puzzle(puzzle)

    solve_sudoku(puzzle)

    print("\nSolved Puzzle:")
    print_puzzle(puzzle)
