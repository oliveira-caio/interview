"""827. Making A Large Island

link: https://leetcode.com/problems/making-a-large-island/

problem: You are given an n x n binary matrix grid. You are allowed to change at
most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with
area = 3.

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with
area = 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def neighbors(row, col):
            positions = {(row - 1, col), (row + 1, col),
                         (row, col - 1), (row, col + 1)}
            available = []
            for r, c in positions:
                if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                    available.append((r, c))
            return available

        def dfs(row, col, _id):
            ans = 1
            grid[row][col] = _id
            for r, c in neighbors(row, col):
                if grid[r][c] == 1:
                    ans += dfs(r, c, _id)
            return ans

        _id = 2; area = {}; ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area[_id] = dfs(i, j, _id)
                    ans = max(ans, area[_id])
                    _id += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    ids = {grid[r][c] for r, c in neighbors(i, j)
                           if grid[r][c] > 1}
                    ans = max(ans, 1 + sum(area[_id] for _id in ids))

        return ans
