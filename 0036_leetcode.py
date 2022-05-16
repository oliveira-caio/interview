"""36. Valid Sudoku

link: https://leetcode.com/problems/valid-sudoku/

problem: Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

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
Output: true

Example 2:
Input: board = 
[
["8","3",".",".","7",".",".",".","."]
["6",".",".","1","9","5",".",".","."]
[".","9","8",".",".",".",".","6","."]
["8",".",".",".","6",".",".",".","3"]
["4",".",".","8",".","3",".",".","1"]
["7",".",".",".","2",".",".",".","6"]
[".","6",".",".",".",".","2","8","."]
[".",".",".","4","1","9",".",".","5"]
[".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row():
            for i in range(len(board)):
                visited = set()
                for j in range(len(board[0])):
                    if board[i][j] in visited:
                        return False
                    elif board[i][j] != '.':
                        visited.add(board[i][j])

            return True

        def check_col():
            for j in range(len(board[0])):
                visited = set()
                for i in range(len(board)):
                    if board[i][j] in visited:
                        return False
                    elif board[i][j] != '.':
                        visited.add(board[i][j])

            return True

        def check_box():
            for i in range(len(board) // 3):
                for j in range(len(board[0]) // 3):
                    visited = set()
                    for k in range(len(board) // 3):
                        for l in range(len(board[0]) // 3):
                            if board[3*i + k][3*j + l] in visited:
                                return False
                            elif board[3*i + k][3*j + l] != '.':
                                visited.add(board[3*i + k][3*j + l])

            return True

        return check_row() and check_col() and check_box()
