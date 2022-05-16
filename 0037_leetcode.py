"""37. Sudoku Solver

link: https://leetcode.com/problems/sudoku-solver/

problem: Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
of the grid.

The '.' character indicates empty cells.

Example 1:
Input: board =
[
["5","3",".",".","7",".",".",".","."]
["6",".",".","1","9","5",".",".","."]
[".","9","8",".",".",".",".","6","."]
["8",".",".",".","6",".",".",".","3"]
["4",".",".","8",".","3",".",".","1"]
["7",".",".",".","2",".",".",".","6"]
[".","6",".",".",".",".","2","8","."]
[".",".",".","4","1","9",".",".","5"]
[".",".",".",".","8",".",".","7","9"]
]
Output:
[
["5","3","4","6","7","8","9","1","2"]
["6","7","2","1","9","5","3","4","8"]
["1","9","8","3","4","2","5","6","7"]
["8","5","9","7","6","1","4","2","3"]
["4","2","6","8","5","3","7","9","1"]
["7","1","3","9","2","4","8","5","6"]
["9","6","1","5","3","7","2","8","4"]
["2","8","7","4","1","9","6","3","5"]
["3","4","5","2","8","6","1","7","9"]
]
Explanation: The input board is shown above and the only valid solution is shown
below:

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check_row(val, pos):
            row, col = pos

            for j in range(len(board[0])):
                if board[row][j] == val:
                    return False

            return True

        def check_col(val, pos):
            row, col = pos

            for i in range(len(board)):
                if board[i][col] == val:
                    return False

            return True

        def check_box(val, pos):
            row, col = pos[0] // 3, pos[1] // 3

            for k in range(len(board) // 3):
                for l in range(len(board[0]) // 3):
                    if board[3*row + k][3*col + l] == val:
                        return False

            return True

        def is_valid(val, pos):
            return (check_row(val, pos) and
                    check_col(val, pos) and
                    check_box(val, pos))

        def find_empty():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        return i, j

        def solve(numbers):
            pos = find_empty()
            if not pos:
                return True
            row, col = pos

            for n in numbers:
                if is_valid(n, pos):
                    board[row][col] = n
                    if solve(numbers):
                        return True
                    board[row][col] = '.'

            return False

        numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        solve(numbers)
