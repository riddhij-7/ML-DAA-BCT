n = 8

def is_safe(board, r, c):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and (i == r or j == c or abs(i - r) == abs(j - c)):
                return False         # same row, same column or same diagonal
    return True

def solve(board, row, first_row):
    if row == n:                     # all rows done
        return True
    if row == first_row:             # this row already has the first queen
        return solve(board, row + 1, first_row)
    for c in range(n):
        if is_safe(board, row, c):
            board[row][c] = 1        # place queen
            if solve(board, row + 1, first_row):
                return True
            board[row][c] = 0        # backtrack
    return False

fr = int(input("Row of first queen (0-7): "))
fc = int(input("Column of first queen (0-7): "))
board = [[0] * n for _ in range(n)]
board[fr][fc] = 1                    # place the first queen

if solve(board, 0, fr):
    print("Final 8-Queens matrix:")
    for row in board:
        print(*row)
else:
    print("No solution with this first queen position")

#Input - 0, then 0 (row 0, column 0)	Output - A valid 8×8 board with the first queen at the top-left