#                     LeetCode 36 --- Sudoku Checker
#
# Goal: Write function which takes in list of rows of length nine and returns
#       whether or not the corresponding sudokuboard is valid

row1 = ['5', '3', '.',    '.', '7', '.',    '.', '.', '.']
row2 = ['6', '.', '.',    '1', '9', '5',    '.', '.', '.']
row3 = ['.', '9', '8',    '.', '.', '.',    '.', '6', '.']

row4 = ['8', '.', '.',    '.', '6', '.',    '.', '.', '3']
row5 = ['4', '.', '.',    '8', '.', '3',    '.', '.', '1']
row6 = ['7', '.', '.',    '.', '2', '.',    '.', '.', '6']

row7 = ['.', '6', '.',    '.', '.', '.',    '2', '8', '.']
row8 = ['.', '.', '.',    '4', '1', '9',    '.', '.', '5']
row9 = ['.', '.', '.',    '.', '8', '.',    '.', '7', '9']

sudokuboard = [ row1,
                row2,
                row3,
                row4,
                row5,
                row6,
                row7,
                row8,
                row9
                ]


# Print the sudoku board so that it looks correct in the terminal.

print "\n \n"

print "   %s %s %s    %s %s %s    %s %s %s " %  (row1[0], row1[1], row1[2],
                                                   row1[3], row1[4], row1[5],
                                                   row1[6], row1[7], row1[8]
                                                    )
print "   %s %s %s    %s %s %s    %s %s %s " %  (row2[0], row2[1], row2[2],
                                                   row2[3], row2[4], row2[5],
                                                   row2[6], row2[7], row2[8]
                                                    )
print "   %s %s %s    %s %s %s    %s %s %s " %  (row3[0], row3[1], row3[2],
                                                   row3[3], row3[4], row3[5],
                                                   row3[6], row3[7], row3[8]
                                                    )
print "\n"

print "   %s %s %s    %s %s %s    %s %s %s " %  (row4[0], row4[1], row4[2],
                                                   row4[3], row4[4], row4[5],
                                                   row4[6], row4[7], row4[8]
                                                    )
print "   %s %s %s    %s %s %s    %s %s %s " %  (row5[0], row5[1], row5[2],
                                                   row5[3], row5[4], row5[5],
                                                   row5[6], row5[7], row5[8]
                                                    )
print "   %s %s %s    %s %s %s    %s %s %s " %  (row6[0], row6[1], row6[2],
                                                   row6[3], row6[4], row6[5],
                                                   row6[6], row6[7], row6[8]
                                                    )
print "\n"

print "   %s %s %s    %s %s %s    %s %s %s " %  (row7[0], row7[1], row7[2],
                                                   row7[3], row7[4], row7[5],
                                                   row7[6], row7[7], row7[8]
                                                    )
print "   %s %s %s    %s %s %s    %s %s %s " %  (row8[0], row8[1], row8[2],
                                                   row8[3], row8[4], row8[5],
                                                   row8[6], row8[7], row8[8]
                                                    )
print "   %s %s %s    %s %s %s    %s %s %s " %  (row9[0], row9[1], row9[2],
                                                   row9[3], row9[4], row9[5],
                                                   row9[6], row9[7], row9[8]
                                                    )
print " \n \n "

# With the board displayed, we now check whether or not it is valid.
# Check if rows are valid
for row in sudokuboard:

    for i in range(0,len(row)):

            if row[i] == '.':
                pass

            else:
                for j in range(i+1,len(row)):

                    if row[i] == row[j]:
                        print "Sudoku board not valid"
                        print "Entries %d and %d in Row %s are equal" % (i+1,j+1,row)
                        exit()
                    else:
                        pass

# Define columns


# count = 0
# col=[]                                     James' better way for indexing
# col[8]                                     columns of the board.
# for row in sudokuboard:
#     col[count].append(row(count))


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
                for j in range(i+1,len(col)):

                    if col[i] == col[j]:
                        print "Sudoku board not valid"
                        print "Entries %d and %d in Column %s are equal" % (i+1,j+1,col)
                        exit()
                    else:
                        pass

# Define the 9 squares. Index row-column i.e. sq23 is square in second row
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
                for j in range(i+1,len(sq)):

                    if sq[i] == sq[j]:
                        print "Sudoku board not valid"
                        print "Square %s has entries that are equal." % sq
                        exit()
                    else:
                        pass

print "This is a valid sudoku board. \n \n "

# Now that the bones of the code have been written, this needs to be written
# inside a function which we can call to check any sudoku board.

def sudokucheck(board): # board is a list of lists each with nine entries

    # First we have the function check whether the rows are valid.

    for row in board:

        for i in range(0,len(row)):

                if row[i] == '.':
                    pass

                else:
                    for j in range(i+1,len(row)):

                        if row[i] == row[j]:
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
                        for j in range(i+1,len(col)):

                            if col[i] == col[j]:
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
                        for j in range(i+1,len(sq)):

                            if sq[i] == sq[j]:
                                #print "Sudoku board not valid"
                                #print "Square %s has entries that are equal." % sq
                                return False
                            else:
                                pass

        #print "True"
        return True
