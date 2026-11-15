def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row - 1 # moves one row upward.
    j = col - 1 # moves one column left.

    while i >= 0 and j >= 0: # Continue checking while row and column are not negative.
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False # If a queen is found, the position is unsafe.
        i -= 1
        j += 1

    return True # If no queen is found, the position is safe.


def solve(board, row, n):

    if row == n: # It indicate that all queen are placed successfully.
        return True

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1 # queen is place

            if solve(board, row+1, n): # trie to place the next queen
                return True

            board[row][col] = 0 # remove the queen if that choice fail

    return False


n = int(input("Enter number of queens: "))

board = [[0 for j in range(n)] for i in range(n)]

# Place first queen
board[0][1] = 1

if solve(board, 1, n):
    print("\nN-Queen Solution:")
    print_board(board, n)
else:
    print("Solution does not exist")