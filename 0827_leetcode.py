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


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def neighbors(row, col):
            directions = {(row - 1, col), (row + 1, col),
                          (row, col - 1), (row, col + 1)}
            for r, c in directions:
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 0:
                    yield r, c
        
        def dfs(row, col, _id, visited):
            stack = [(row, col)]
            visited.add((row, col))
            size = 0
            while stack:
                r, c = stack.pop()
                size += 1
                grid[r][c] = _id
                for neighbor in neighbors(r, c):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            return size
        
        result = 0; _id = 2
        visited = set()
        islands = dict()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    size = dfs(i, j, _id, visited)
                    result = max(size, result)
                    islands[_id] = size
                    _id += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    seen = {grid[r][c] for r, c in neighbors(i, j)}
                    size = 1 + sum((islands[_id] for _id in seen))
                    result = max(size, result)
        
        return result
