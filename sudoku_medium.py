# This script (normally) solves sudoku puzzles "ranked medium"
from sudoku_aux import *
import timeit

# This script has a different approach to the "sudoku_easy.py" script. It took
# me awhile to make it work, but all the bugs are gone. It solves every
# sudoku that I give it the time to solve. Some have taken too long. See the
# "Everest" stated below.


# This board is considered to be of "medium" difficulty by the source website.
# it took 34 seconds to complete.
# row1 = ['.', '.', '.',    '.', '.', '8',    '.', '3', '.']
# row2 = ['.', '.', '.',    '.', '.', '.',    '4', '.', '5']
# row3 = ['.', '.', '1',    '.', '.', '.',    '.', '7', '.']
#
# row4 = ['7', '3', '.',    '.', '.', '.',    '2', '8', '.']
# row5 = ['9', '5', '.',    '3', '.', '.',    '.', '.', '.']
# row6 = ['.', '.', '.',    '.', '.', '6',    '.', '.', '4']
#
# row7 = ['8', '.', '.',    '1', '4', '.',    '.', '.', '.']
# row8 = ['.', '.', '.',    '8', '7', '.',    '.', '1', '6']
# row9 = ['.', '.', '5',    '.', '.', '.',    '9', '.', '.']

# The puzzles below are the final test. Can the code solve a "hard" puzzle?
# This puzzle required 3 seconds to complete.
# row1 = ['.', '3', '.',    '9', '5', '.',    '8', '.', '.']
# row2 = ['.', '.', '.',    '.', '.', '.',    '.', '9', '.']
# row3 = ['9', '.', '.',    '8', '.', '6',    '.', '4', '.']
#
# row4 = ['6', '8', '.',    '.', '3', '.',    '.', '.', '.']
# row5 = ['.', '.', '7',    '.', '2', '.',    '3', '.', '.']
# row6 = ['.', '.', '.',    '.', '7', '.',    '.', '5', '4']
#
# row7 = ['.', '2', '.',    '5', '.', '4',    '.', '.', '7']
# row8 = ['.', '5', '.',    '.', '.', '.',    '.', '.', '.']
# row9 = ['.', '.', '4',    '.', '6', '7',    '.', '1', '.']

# This puzzle required 42 seconds to complete.
# row1 = ['.', '4', '1',    '.', '.', '.',    '.', '.', '.']
# row2 = ['.', '.', '8',    '1', '7', '.',    '.', '.', '3']
# row3 = ['.', '.', '.',    '.', '3', '.',    '6', '.', '1']
#
# row4 = ['4', '.', '.',    '.', '.', '3',    '2', '.', '.']
# row5 = ['.', '5', '.',    '.', '.', '.',    '.', '9', '.']
# row6 = ['.', '.', '2',    '8', '.', '.',    '.', '.', '6']
#
# row7 = ['5', '.', '4',    '.', '6', '.',    '.', '.', '.']
# row8 = ['8', '.', '.',    '.', '5', '2',    '7', '.', '.']
# row9 = ['.', '.', '.',    '.', '.', '.',    '9', '3', '.']


# The Telegraph published the following "Everest of numerical games" and called
# it the hardest sudoku puzzle on earth...

# Arto Inkala, a mathematician from Finland, designed it to be extremly
# difficult. On the normal scale sudoku are ranked easiest at 1 upto 5
# as the hardest. This puzzle is an 11 on that scale... This code solved
# Inkala's sudoku in 1hour and 10minutes.

# row1 = ['8', '.', '.',    '.', '.', '.',    '.', '.', '.']
# row2 = ['.', '.', '3',    '6', '.', '.',    '.', '.', '.']
# row3 = ['.', '7', '.',    '.', '9', '.',    '2', '.', '.']
#
# row4 = ['.', '5', '.',    '.', '.', '7',    '.', '.', '.']
# row5 = ['.', '.', '.',    '.', '4', '5',    '7', '.', '.']
# row6 = ['.', '.', '.',    '1', '.', '.',    '.', '3', '.']
#
# row7 = ['.', '.', '1',    '.', '.', '.',    '.', '6', '8']
# row8 = ['.', '.', '8',    '5', '.', '.',    '.', '1', '.']
# row9 = ['.', '9', '.',    '.', '.', '.',    '4', '.', '.']

# After 1hour and 10minutes, the code returned...
# row1 = ['8', '1', '2',    '7', '5', '3',    '6', '4', '9']
# row2 = ['9', '4', '3',    '6', '8', '2',    '1', '7', '5']
# row3 = ['6', '7', '5',    '4', '9', '1',    '2', '8', '3']
#
# row4 = ['1', '5', '4',    '2', '3', '7',    '8', '9', '6']
# row5 = ['3', '6', '9',    '8', '4', '5',    '7', '2', '1']
# row6 = ['2', '8', '7',    '1', '6', '9',    '5', '3', '4']
#
# row7 = ['5', '2', '1',    '9', '7', '4',    '3', '6', '8']
# row8 = ['4', '3', '8',    '5', '2', '6',    '9', '1', '7']
# row9 = ['7', '9', '6',    '3', '1', '8',    '4', '5', '2']

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

# The heart of the script starts from here.

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
