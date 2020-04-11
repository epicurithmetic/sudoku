# Learning recursion via Sudoku solver


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


puzzle = [
    [8, 8, 0,    0, 0, 0,    0, 0, 0],
    [0, 0, 3,    6, 0, 0,    0, 0, 0],
    [0, 7, 0,    0, 9, 0,    2, 0, 0],
    [0, 5, 0,    0, 0, 7,    0, 0, 0],
    [0, 0, 0,    0, 4, 5,    7, 0, 0],
    [0, 0, 0,    1, 0, 0,    0, 3, 0],
    [0, 0, 1,    0, 0, 0,    0, 6, 8],
    [0, 0, 0,    5, 0, 0,    0, 1, 0],
    [0, 9, 0,    0, 0, 0,    4, 0, 0]
]


def print_board(board):

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

def find_empty(board):

    for i in range(len(board)):
        for j in range(len(board[0])):

            if board[i][j] == 0:

                return (i,j) # row, col

    return None

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(board):

    find = find_empty(board)

    if find == None:
        return True
    else:
        row, col = find


    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True

        board[row][col] = 0

    return False

print_board(puzzle)
solve(puzzle)
print_board(puzzle)
