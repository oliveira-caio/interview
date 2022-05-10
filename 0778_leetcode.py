"""778. Swim in Rising Water

link: https://leetcode.com/problems/swim-in-rising-water/

problem: You are given an n x n integer matrix grid where each value grid[i][j]
represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You
can swim from a square to another 4-directionally adjacent square if and only if
the elevation of both squares individually are at most t. You can swim infinite
distances in zero time. Of course, you must stay within the boundaries of the
grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1)
if you start at the top left square (0, 0).

Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a
higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:
Input: grid =
[[0,1,2,3,4],
[24,23,22,21,5],
[12,13,14,15,16],
[11,17,18,19,20],
[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n^2
Each value grid[i][j] is unique.
"""


from heapq import *


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def neighbors(r, c):
            dirs = {(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)}
            for nr, nc in dirs:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    yield nr, nc

        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        ans = 0

        while heap:
            time, row, col = heappop(heap)
            ans = max(time, ans)
            if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                return ans
            for nr, nc in neighbors(row, col):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heappush(heap, (grid[nr][nc], nr, nc))
