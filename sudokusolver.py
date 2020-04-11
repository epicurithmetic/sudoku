# Script solves sudoku puzzles. Longest time so far is ~30min.
from sudoku_aux import *
import timeit


# Entering the sudokuboard directly into the script is cumbersome. The following
# script will try to make the user interface more user-friendly.

sudokuboard = []
print('\nSudoku Solver: \n')
print('Please enter each row from top-to-bottom. Indicating empty entries')
print('using the number 0. Otherwise, entering the number in the square.')

# Boolean used to make sure the correct puzzle is being solved.
# This will help deal with nonsense input from the user.
correct_sudoku_puzzle = False

while correct_sudoku_puzzle == False:

    # Take the input from the user.
    for i in range(1,10):
        print("Row %s" % i)
        row = input("")
        # Now the code wraps the input into the design choice made at the start of
        # writing this project.
        row = list(row)
        row_board = []
        for x in row:
            if x == '0':
                row_board.append('.')
            else:
                row_board.append(x)
        sudokuboard.append(row_board)

    # Print the board
    print("\nIs this the board that you would like me to solve?")
    print(print_sudoku(sudokuboard))

    correct_board = input("Is the board correct?(Y/n): ")
    if correct_board == 'Y':
        correct_sudoku_puzzle = True
    elif correct_board == 'n':
        print('Please enter the board again. Remembering to enter empty squares')
        print('as the number 0.')
    else:
        print('Sorry, I did not understand that. ')
        print('Please enter the board again. Remembering to enter empty squares')
        print('as the number 0.')


# Before we get started, we should check whether the given board is valid.
if sudokucheck(sudokuboard) == False:
    print("The board is not valid")
    exit()
else:
    pass

# Work work work work work ...
print('\nThinking ... \n')
start = timeit.default_timer()
updated_board = sudoku_tree_solver(sudokuboard)
stop = timeit.default_timer()


if sudoku_complete(updated_board):
    print('Here is the solution to your sudoku.')
    print_sudoku(updated_board)
    print('It took %s seconds to solve this Sudoku' % (stop - start))
else:
    print('Hmmm. I seem to be stuck. I need a smarter person to code me better.')
