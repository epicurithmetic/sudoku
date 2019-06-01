# Script solves sudoku puzzles. Longest time so far is ~30min.
from sudoku_aux import *
import timeit



# Enter the sudoku puzzle to be solved in the grid below.
row1 = ['8', '.', '.',    '.', '.', '.',    '.', '.', '.']
row2 = ['.', '.', '3',    '6', '.', '.',    '.', '.', '.']
row3 = ['.', '7', '.',    '.', '9', '.',    '2', '.', '.']

row4 = ['.', '5', '.',    '.', '.', '7',    '.', '.', '.']
row5 = ['.', '.', '.',    '.', '4', '5',    '7', '.', '.']
row6 = ['.', '.', '.',    '1', '.', '.',    '.', '3', '.']

row7 = ['.', '.', '1',    '.', '.', '.',    '.', '6', '8']
row8 = ['.', '.', '8',    '5', '.', '.',    '.', '1', '.']
row9 = ['.', '9', '.',    '.', '.', '.',    '4', '.', '.']

# Defines the board the script will solve.
sudokuboard = [row1,
               row2,
               row3,
               row4,
               row5,
               row6,
               row7,
               row8,
               row9
               ]

# The heart of the script starts from here...

# Print the board
print "This is the board to be solved."
print print_sudoku(sudokuboard)

# Before we get started, we should check whether the given board is valid.
if sudokucheck(sudokuboard) == False:
    print "The board is not valid"
    exit()
else:
    pass

# Work work work work work ...
print '\nThinking ... \n'
start = timeit.default_timer()
updated_board = sudoku_tree_solver(sudokuboard)
stop = timeit.default_timer()


if sudoku_complete(updated_board):
    print '... and Done.'
    print_sudoku(updated_board)
    print 'It took %s seconds to solve this Sudoku' % (stop - start)
else:
    print 'Hmmm. I seem to be stuck. I need a smarter person to code me better.'
