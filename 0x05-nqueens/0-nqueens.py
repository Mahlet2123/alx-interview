#!/usr/bin/python3
""" 0-nqueens module """
import sys


def is_safe(board, row, col, N):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N, board, row):
    if row == N:
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    print(f'[{i}, {j}]', end='')
        print()
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(N, board, row + 1)
            board[row][col] = 0


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number\n")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4\n")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(N, board, 0)


if __name__ == "__main__":
    main()
