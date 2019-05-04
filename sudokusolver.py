import timeit
# Goal: write a script that solves a given sudoku board.

# This code will require the sudoku checker function
def sudokucheck(board): # board is a list of lists each with nine entries

    """
        This function checks whether a board is valid. Not necessarily
        complete, but that the rules have not yet been broken.

    """

    # First we have the function check whether the rows are valid.
    for row in board:

        for i in range(0,len(row)):

                if row[i] == '.':
                    pass

                else:
                    for j in range(0,len(row)):
                        if i == j:
                            pass
                        elif row[i] == row[j]:
                            #print "Sudoku board not valid"
                            #print "Entries %d and %d in Row %s are equal" % (i+1,j+1,row)
                            #valid = False
                            #print i,j, 'row'
                            return False
                        else:
                            pass

        # Define columns of board

        col1 =[]
        for row in sudokuboard:
            col1.append(row[0])

        col2 =[]
        for row in sudokuboard:
            col2.append(row[1])

        col3 =[]
        for row in sudokuboard:
            col3.append(row[2])

        col4 =[]
        for row in sudokuboard:
            col4.append(row[3])

        col5 =[]
        for row in sudokuboard:
            col5.append(row[4])

        col6 =[]
        for row in sudokuboard:
            col6.append(row[5])

        col7 =[]
        for row in sudokuboard:
            col7.append(row[6])

        col8 =[]
        for row in sudokuboard:
            col8.append(row[7])

        col9 =[]
        for row in sudokuboard:
            col9.append(row[8])

        columns = [col1,
                   col2,
                   col3,
                   col4,
                   col5,
                   col6,
                   col7,
                   col8,
                   col9
                   ]

        # Check columns are valid
        for col in columns:

            for i in range(0,len(col)):

                    if col[i] == '.':
                        pass

                    else:
                        for j in range(0,len(col)):
                            if i == j:
                                pass
                            elif col[i] == col[j]:
                                #print "Sudoku board not valid"
                                #print "Entries %d and %d in Column %s are equal" % (i+1,j+1,col)
                                #print i,j, 'col'
                                return False
                            else:
                                pass



        #Define the 9 squares. Index row-column i.e. sq23 is square in second row
        # and third column of squares.
        # First column of 3x3 squares
        sq11 = [row1[0],row1[1],row1[2],
                row2[0],row2[1],row2[2],
                row3[0],row3[1],row3[2]
               ]

        sq12 = [row4[0],row4[1],row4[2],
                row5[0],row5[1],row5[2],
                row6[0],row6[1],row6[2]
               ]

        sq13 = [row7[0],row7[1],row7[2],
                row8[0],row8[1],row8[2],
                row9[0],row9[1],row9[2]
               ]
        # Second column of 3x3 squares

        sq21 = [row1[3],row1[4],row1[5],
                row2[3],row2[4],row2[5],
                row3[3],row3[4],row3[5]
               ]

        sq22 = [row4[3],row4[4],row4[5],
                row5[3],row5[4],row5[5],
                row6[3],row6[4],row6[5]
               ]

        sq23 = [row7[3],row7[4],row7[5],
                row8[3],row8[4],row8[5],
                row9[3],row9[4],row9[5]
               ]
        # Third column of 3x3 squares

        sq31 = [row1[6],row1[7],row1[8],
                row2[6],row2[7],row2[8],
                row3[6],row3[7],row3[8]
               ]

        sq32 = [row4[6],row4[7],row4[8],
                row5[6],row5[7],row5[8],
                row6[6],row6[7],row6[8]
               ]

        sq33 = [row7[6],row7[7],row7[8],
                row8[6],row8[7],row8[8],
                row9[6],row9[7],row9[8]
               ]

        squares = [sq11,
                   sq12,
                   sq13,
                   sq21,
                   sq22,
                   sq23,
                   sq31,
                   sq32,
                   sq33
                   ]

        for sq in squares:

            for i in range(0,len(sq)):

                    if sq[i] == '.':
                        pass

                    else:
                        for j in range(0,len(sq)):
                            if i == j:
                                pass
                            elif sq[i] == sq[j]:
                                #print "Sudoku board not valid"
                                #print "Square %s has entries that are equal." % sq
                                #print sq
                                return False
                            else:
                                pass

        #print "True"
        return True

# The following function will be determine whether or not the board
# is complete.
def sudoku_complete(board):
    """
        This function returns a Boolean based on whether or not the
        board is finished.

    """

    # Search through rows
    for i in range(0,9):
        for j in range(0,9):

            if board[i][j] == '.':
                return False
            else:
                pass

    return sudokucheck(board)

# This code prints the board in a terminal-friendly fashion
def print_sudoku(board):

    """
        Print a sudoku board in a manner that looks nice in the terminal

    """
    print ' \n '
    print ' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[0][0],board[0][1],board[0][2],board[0][3],board[0][4],board[0][5],board[0][6],board[0][7],board[0][8])
    print ' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[1][0],board[1][1],board[1][2],board[1][3],board[1][4],board[1][5],board[1][6],board[1][7],board[1][8])
    print ' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[2][0],board[2][1],board[2][2],board[2][3],board[2][4],board[2][5],board[2][6],board[2][7],board[2][8])
    print '------------------------------------'
    print '------------------------------------'
    print ' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[3][0],board[3][1],board[3][2],board[3][3],board[3][4],board[3][5],board[3][6],board[3][7],board[3][8])
    print ' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[4][0],board[4][1],board[4][2],board[4][3],board[4][4],board[4][5],board[4][6],board[4][7],board[4][8])
    print ' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[5][0],board[5][1],board[5][2],board[5][3],board[5][4],board[5][5],board[5][6],board[5][7],board[5][8])
    print '------------------------------------'
    print '------------------------------------'
    print ' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[6][0],board[6][1],board[6][2],board[6][3],board[6][4],board[6][5],board[6][6],board[6][7],board[6][8])
    print ' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[7][0],board[7][1],board[7][2],board[7][3],board[7][4],board[7][5],board[7][6],board[7][7],board[7][8])
    print ' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[8][0],board[8][1],board[8][2],board[8][3],board[8][4],board[8][5],board[8][6],board[8][7],board[8][8])

    return ' \n '

#
# The following boards can be solved without branching.
#

# row1 = ['5', '3', '.',    '.', '7', '.',    '.', '.', '.']
# row2 = ['6', '.', '.',    '1', '9', '5',    '.', '.', '.']
# row3 = ['.', '9', '8',    '.', '.', '.',    '.', '6', '.']
#
# row4 = ['8', '.', '.',    '.', '6', '.',    '.', '.', '3']
# row5 = ['4', '.', '.',    '8', '.', '3',    '.', '.', '1']
# row6 = ['7', '.', '.',    '.', '2', '.',    '.', '.', '6']
#
# row7 = ['.', '6', '.',    '.', '.', '.',    '2', '8', '.']
# row8 = ['.', '.', '.',    '4', '1', '9',    '.', '.', '5']
# row9 = ['.', '.', '.',    '.', '8', '.',    '.', '7', '9']

# row1 = ['3', '2', '8',    '.', '7', '.',    '.', '1', '5']
# row2 = ['.', '7', '6',    '.', '.', '.',    '8', '9', '3']
# row3 = ['4', '.', '.',    '1', '.', '.',    '.', '6', '.']
#
# row4 = ['5', '.', '.',    '3', '.', '.',    '.', '7', '.']
# row5 = ['.', '.', '.',    '8', '1', '.',    '6', '3', '.']
# row6 = ['6', '.', '.',    '.', '4', '.',    '9', '.', '.']
#
# row7 = ['.', '6', '2',    '5', '9', '7',    '.', '.', '.']
# row8 = ['9', '.', '.',    '.', '3', '.',    '7', '.', '.']
# row9 = ['7', '4', '3',    '.', '2', '1',    '.', '8', '.']


#
# These boards require some branching of options to solve.
#

#
# This medium board is solved by the tree solver.
#

# "Medium" sudoku puzzle.

row1 = ['.', '.', '.',    '.', '.', '8',    '.', '3', '.']
row2 = ['.', '.', '.',    '.', '.', '.',    '4', '.', '5']
row3 = ['.', '.', '1',    '.', '.', '.',    '.', '7', '.']

row4 = ['7', '3', '.',    '.', '.', '.',    '2', '8', '.']
row5 = ['9', '5', '.',    '3', '.', '.',    '.', '.', '.']
row6 = ['.', '.', '.',    '.', '.', '6',    '.', '.', '4']

row7 = ['8', '.', '.',    '1', '4', '.',    '.', '.', '.']
row8 = ['.', '.', '.',    '8', '7', '.',    '.', '1', '6']
row9 = ['.', '.', '5',    '.', '.', '.',    '9', '.', '.']

#
# So far, my branching does not solve this sudoku.
#

# "Hard" sudoku puzzle.

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

start = timeit.default_timer()

# Print the board
print print_sudoku(sudokuboard)
print "This is the board to be solved."

# Before we get started, we should check whether the given board is valid.
if sudokucheck(sudokuboard) == False:
    print "The board is not valid"
    exit()
else:
    pass

# This function will allow us to find the possible entries for each point
# of the sudokuboard.
def sudoku_array_allowed(board):

    """
        Given a sudoku board --- in the form of a list of 9 element lists --- this
        function will return an array indexed by row (i) and column(j) of allowed
        numbers at each entry of the sudoku board.

        To be precise; the output is a list of nine lists --- the list of rows.
        Each element in a row is a list of allowed entries at the point of the
        board.

        Empty spots are to be entered as the string '.'

        If the board already has an entry, then the allowed entries will be
        an empty list at that index.

    """

    # This is a list of elements initially in each row.
    initial_row_entries = []

    for row in board:

        initial = []

        for i in range(0, len(row)):

            if row[i] == '.':
                pass
            else:
                initial.append(row[i])

        initial_row_entries.append(initial)



    # This creates a list of elements initially missing in each row.
    initial_row_missing = []

    for list in initial_row_entries:
        missing = []
        for i in range(1,10):
            if not(str(i) in list):
                missing.append(str(i))
            else:
                pass
        initial_row_missing.append(missing)

    array_allowed_entries = []

    # Index over the rows of the board:
    for i in range(0,9):

        row_allowed_entries = []

        # Index over the elements of the row.
        for j in range(0,9):

            # Create list of entries allowed at i,j.
            local_allowed_entries = []

            # If i,j is empty, then try elements missing from row.
            if board[i][j] == '.':

                for x in initial_row_missing[i]:
                    board[i][j] = x
                    if sudokucheck(board) == True:
                        # Append the elements if they are allowed.
                        local_allowed_entries.append(x)
                    else:
                        pass
                    board[i][j] = '.'
            else:
                pass

            row_allowed_entries.append(local_allowed_entries)

        array_allowed_entries.append(row_allowed_entries)

    return array_allowed_entries

# As a first pass we fill in all entries with only one possible
# option. Run the sudoku_array_allowed function on the new board. Repeating
# this until we have to make a choice about which element to put in a square.
# This procedure is packaged in the next function.
def sudoku_oneoption(board):

    """
        This function takes in a sudokuboard. Finds the possible entries
        at each point in the board. Fills in those points with only one
        possibility. Repeats the check and fill until the board is full or
        the solver must fork into branches of choices.

    """

    # This Boolean is true while there are points with precisely one option.
    one_option = True

    # This is the array of allowed entries at each point of the board.
    array_allowed_entries = sudoku_array_allowed(board)

    # This while loop does the checking and filling.
    while one_option == True:

        # Index over rows
        for i in range(0,9):

            # Index over columns
            for j in range(0,9):

                # This if statement fills the points with one possible entry.
                if len(array_allowed_entries[i][j]) == 1:
                    board[i][j] = array_allowed_entries[i][j][0]
                else:
                    pass

        # Is it still true that there is only one option?
        # Recalculate the allowed entries on the new board.
        array_allowed_entries = sudoku_array_allowed(board)

        # After rechecking the board, we look for points with one possible
        # entry.
        length_one = 0
        for i in range(0,9):
            for j in range(0,9):
                if len(array_allowed_entries[i][j]) == 1:
                    length_one = 1
                else:
                    pass

        # If there are none, then we use the Boolean to exit the while loop.
        # Else, we go through the loop again.
        if length_one == 1:
            pass
        else:
            one_option = False

    # Print the sudokuboard. Return empty string to avoid the "none"
    #print print_sudoku(board)
    return None

# This does the work.
sudoku_oneoption(sudokuboard)
stop = timeit.default_timer()

# Print the work done so far.
if sudoku_complete(sudokuboard):
    print 'This board has been solved.'
    print_sudoku(sudokuboard)
    print 'Time: ', stop - start, 'seconds'
else:
    print_sudoku(sudokuboard)
    print 'More work needs to be done to complete this board.'

# Conceivably, this could solve the sudoku. However, in general, this will not
# be enough to fill the board completely. We will require some branching
# procedure to follow different choices until an error occurs.

# Find entry with minimum number of options to make.
def sudoku_min_option(board):

    """
        This function returns the minimum number of options among all
        the squares of the sudoku board.

        For instance if a board has a square with only two options, while all
        other squares have more than two options, then this function
        will return 2.

    """
    #Array of allowed entries
    allow = sudoku_array_allowed(board)

    all_zero = True
    for x in allow:
        if not (len(x) == 0):
            all_zero = False
        else:
            pass

    if all_zero == True:
        return 0

    # Local variable to find the entries with smallest options.
    min_length = 9

    # Row index
    for i in range(0,9):
        # Column index
        for j in range(0,9):

            # Update minimum length and the index of the entry with
            # the minimun length.
            if 0 < len(allow[i][j]) < min_length:
                min_length = len(allow[i][j])

    return min_length

#
# Attempt at recursive solver. Don't know how to back-track. Does not work.
#
# def sudoku_iter(board):
#
#     # Array of allowed entries
#     allow = sudoku_array_allowed(board)
#
#     # Local variables to find the entries with smallest options.
#     min_index_row = 0
#     min_index_col = 0
#     min_length = 9
#
#     # Now we find the entry with the smallest number of options.
#     next_entry = []
#     # Row index
#     for i in range(0,9):
#         # Column index
#         for j in range(0,9):
#
#             # Update minimum length and the index of the entry with
#             # the minimun length.
#             if 0 < len(allow[i][j]) < min_length:
#                 min_length = len(allow[i][j])
#                 min_index_row = i
#                 min_index_col = j
#                 # Entry with lowest number of options.
#                 next_entry = allow[min_index_row][min_index_col]
#                 #print next_entry
#
#     # Loop the options at this entry.
#     for x in next_entry:
#         board[min_index_row][min_index_col] = x
#         print_sudoku(board)
#         if (sudoku_min_option(board) == 0 and (not sudoku_complete(board))):
#         # In this case we want to return the board at its previous
#         # iteration.
#             pass
#
#         elif sudoku_complete(board):
#             return print_sudoku(board)
#
#         else:
#             sudoku_iter(board)

def sudoku_tree_solver(board):

    """
        Given a board, this function creates a list containing that board.

        For each board (seed) in the list, this function updates the list by adjoining
        new boards. These are obtained by taking the smallest options and making
        all of them seperately. The seed is removed each time.

        Each step updates the list with boards with valid entries.

    """
    tree = [board]
    solved = False
    solution = []

    while solved == False:

        # Remove any invalid boards.
        for brd in tree:
            if not sudokucheck(brd):
                tree.remove(brd)
            else:
                pass

        if len(tree) == 0:
            print "Tree length zero; something went wrong."
            exit()

        for brd in tree:

                # For each board in the tree. Find entry with smallest number
                # of options. Append each of those options to the tree.
                # Remove the board from the tree.

                if sudoku_complete(brd):
                    solved = True
                    solution = brd

                # Remove brd
                tree.remove(brd)

                # Array of allowed entries
                allow = sudoku_array_allowed(brd)

                # Local variables to find the entries with smallest options.
                min_index_row = 0
                min_index_col = 0
                min_length = 9

                # Now we find the entry with the smallest number of options.
                next_entry = []
                # Row index
                for i in range(0,9):
                    # Column index
                    for j in range(0,9):

                        # Update minimum length and the index of the entry with
                        # the minimun length.
                        if 0 < len(allow[i][j]) < min_length:
                            min_length = len(allow[i][j])
                            min_index_row = i
                            min_index_col = j
                            # Entry with lowest number of options.
                            next_entry = allow[min_index_row][min_index_col]

                # Problem with this implementation due to the way
                # lists are stored in memory. Renaming lists does not
                # create a new list.

                # In order to solve this problem I must initialize
                # as many lists as there are objects in next_entry.
                # Each of which is different from brd only at the
                # entry found above.

                for x in next_entry:
                    a = list(brd)
                    a[min_index_row][min_index_col] = x
                    tree.append(a)

                    # print "Length of tree", len(tree)
                    # #Print boards as we go to see what the code is doing
                    # print '----- Tree -----'
                    # for brd in tree:
                    #     print_sudoku(brd)
                    # print len(tree)
                    # print '---------------- \n\n\n'

    print "Done."
    return print_sudoku(solution)

start = timeit.default_timer()
sudoku_tree_solver(sudokuboard)
stop = timeit.default_timer()
print 'Time: ', stop - start, 'seconds'
