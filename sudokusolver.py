# Goal: write a script that solves a given sudoku board.

# This code will require the sudoku checker function
def sudokucheck(board): # board is a list of lists each with nine entries

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
        return True # board is a list of lists each with nine entries

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
                                return False
                            else:
                                pass

        #print "True"
        return True

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
    print ' \n '

# The example board is from LeetCode.

row1 = ['5', '3', '.',    '.', '7', '.',    '.', '.', '.']
row2 = ['6', '.', '.',    '1', '9', '5',    '.', '.', '.']
row3 = ['.', '9', '8',    '.', '.', '.',    '.', '6', '.']

row4 = ['8', '.', '.',    '.', '6', '.',    '.', '.', '3']
row5 = ['4', '.', '.',    '8', '.', '3',    '.', '.', '1']
row6 = ['7', '.', '.',    '.', '2', '.',    '.', '.', '6']

row7 = ['.', '6', '.',    '.', '.', '.',    '2', '8', '.']
row8 = ['.', '.', '.',    '4', '1', '9',    '.', '.', '5']
row9 = ['.', '.', '.',    '.', '8', '.',    '.', '7', '9']

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

# Print the board
print print_sudoku(sudokuboard)

# Before we get started, we should check whether the given board is valid.
if sudokucheck(sudokuboard) == False:
    print "The board is not valid"
    exit()
else:
    pass



# This is a list of elements initially in each row.
initial_row_entries = []

for row in sudokuboard:

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


print initial_row_missing


# Next we obtain the list of allowed entries at EACH point in the table. This
# will be a sublist (at each point) of initial_row_missing, as some of
# those values may return invalid boards.

# array_allowed_entries = []
#
# # Index over the rows of the board:
# for i in range(0,9):
#
#     row_allowed_entries = []
#
#     # Index over the elements of the row
#     for j in range(0,9):
#         local_allowed_entries = []
#         if sudokuboard[i][j] == '.':
#
#             for x in initial_row_missing[i]:
#                 sudokuboard[i][j] = x
#                 if sudokucheck(sudokuboard) == True:
#                     local_allowed_entries.append(x)
#                 else:
#                     pass
#                 sudokuboard[i][j] = '.'
#         else:
#             pass
#
#         row_allowed_entries.append(local_allowed_entries)
#
#     array_allowed_entries.append(row_allowed_entries)


# Package this code into a function which outputs the array of allowed entries
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

    array_allowed_entries = []

    # Index over the rows of the board:
    for i in range(0,9):

        row_allowed_entries = []

        # Index over the elements of the row
        for j in range(0,9):
            local_allowed_entries = []
            if board[i][j] == '.':

                for x in initial_row_missing[i]:
                    board[i][j] = x
                    if sudokucheck(board) == True:
                        local_allowed_entries.append(x)
                    else:
                        pass
                    board[i][j] = '.'
            else:
                pass

            row_allowed_entries.append(local_allowed_entries)

        array_allowed_entries.append(row_allowed_entries)

    return array_allowed_entries

array_allowed_entries = sudoku_array_allowed(sudokuboard)
# As a first pass we might try and fill in all entries with only one possible
# option. Run the sudoku_array_allowed function on the new board. Repeating
# this until we have to make a choice about which element to put in a square.

one_option = True

while one_option == True:

    # Index over rows
    for i in range(0,9):

        # Index over columns
        for j in range(0,9):

            if len(array_allowed_entries[i][j]) == 1:
                sudokuboard[i][j] = array_allowed_entries[i][j][0]
            else:
                pass

    # Is it still true that there is only one option?

    # Recalculate the allowed entries on the new board
    array_allowed_entries = sudoku_array_allowed(sudokuboard)

    length_one = 0

    for i in range(0,9):
        for j in range(0,9):
            if len(array_allowed_entries[i][j]) == 1:
                length_one = 1
            else:
                pass

    if length_one == 1:
        pass
    else:
        one_option = False

print print_sudoku(sudokuboard)
print sudoku_array_allowed(sudokuboard)


# Conceivably, this could solve the sudoku. However, in general, this will not
# be enough to fill the board completely. We will require some branching
# procedure to follow different choices until an error occurs.
