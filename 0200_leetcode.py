"""200. Number of Islands

link: https://leetcode.com/problems/number-of-islands/

problem: Given an m x n 2D binary grid grid which represents a map of '1's
(land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def neighbors(r, c):
            dirs = {(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)}
            for nr, nc in dirs:
                if (0 <= nr < len(grid) and
                    0 <= nc < len(grid[0]) and
                    grid[nr][nc] == '1'):
                    yield nr, nc

        def bfs(r, c, visited):
            queue = collections.deque([(r, c)])
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()
                for nr, nc in neighbors(r, c):
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                    
        visited = set()
        answer = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    answer += 1
                    bfs(i, j, visited)
                    
        return answer
