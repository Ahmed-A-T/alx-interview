#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_error_and_exit(message):
    print(message)
    sys.exit(1)

def is_safe(board, row, col, N):
    # Check this column on upper rows
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N):
    if row >= N:
        print(" ".join(str(col) for col in board))
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)
            board[row] = -1

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    main()
