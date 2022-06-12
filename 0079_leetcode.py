"""79. Word Search

link: https://leetcode.com/problems/word-search/

problem: Given an m x n grid of characters board and a string word, return true
if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

Example 1:
Input:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a
larger board?
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def neighbors(r, c):
            dirs = {(r-1, c), (r+1, c), (r, c-1), (r, c+1)}
            for nr, nc in dirs:
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    yield nr, nc

        def solve(row, col, letter, visited):
            if letter == len(word):
                return True

            for nr, nc in neighbors(row, col):
                if board[nr][nc] == word[letter] and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    check = solve(nr, nc, letter + 1, visited)
                    if check:
                        return True
                    visited.remove((nr, nc))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = {(i, j)}
                    check = solve(i, j, 1, visited)
                    if check:
                        return True

        return False
