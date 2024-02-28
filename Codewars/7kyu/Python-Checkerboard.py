"""
DESCRIPTION:
You are trying to make a checkerboard made up of X's and O's. You've implemented the function before in a different language but it just won't work. The function creates an n by n board of X's and O's.

For example (Input --> Output)

n = 4 -->
[['X', 'O', 'X', 'O'],
 ['O', 'X', 'O', 'X'],
 ['X', 'O', 'X', 'O'],
 ['O', 'X', 'O', 'X']]

"""

# first_solution
def make_checkered_board(n):
    line=['X' for x in range(n)]
    board = [line[:] for y in range(n)]
    for row in range(0,n):
        for col in range(0,n):
            if (row+col)%2:
                board[row][col]="O"
    for line in board:
        print(line)
    return board

#second-solution
def make_checkered_board(n):
    board =[['X' for _ in range(n)] for _ in range(n) ]
    for row in range(0,n):
        for col in range(0,n):
            if (row+col)%2:
                board[row][col]="O"
    for line in board:
        print(line)
    return board