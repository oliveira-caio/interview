"""317. Shortest Distance from All Buildings

problem: You are given an m x n grid grid of values 0, 1, or 2, where:

- each 0 marks an empty land that you can pass by freely,
- each 1 marks a building that you cannot pass through, and
- each 2 marks an obstacle that you cannot pass through.

You want to build a house on an empty land that reaches all buildings in the
shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to
build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the
friends and the meeting point.

The distance is calculated using Manhattan Distance, where
distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example 1:
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at
(0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel
distance of 3+3+1=7 is minimal.
So return 7.

Example 2:
Input: grid = [[1,0]]
Output: 1

Example 3:
Input: grid = [[1]]
Output: -1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0, 1, or 2.
There will be at least one building in the grid.
"""


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def neighbors(r, c):
            directions = {(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)}

            for nr, nc in directions:
                if (0 <= nr < len(grid) and
                    0 <= nc < len(grid[0]) and
                    grid[nr][nc] == 0):
                    yield nr, nc

        def bfs(row, col, distances):
            queue = deque([(row, col, 0)])
            curr_reach = set()

            while queue:
                curr_row, curr_col, curr_dist = queue.popleft()
                for nr, nc in neighbors(curr_row, curr_col):
                    if (nr, nc) not in curr_reach:
                        distances[nr][nc] += 1 + curr_dist
                        curr_reach.add((nr, nc))
                        queue.append((nr, nc, 1 + curr_dist))

            return curr_reach

        reachable = set()
        distances = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        min_dist = float('inf')

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_reach = bfs(i, j, distances)
                    if not curr_reach:
                        return -1
                    if not reachable:
                        reachable = reachable.union(curr_reach)
                    else:
                        reachable = reachable.intersection(curr_reach)
                    if not reachable:
                        return -1

        for row, col in reachable:
            min_dist = min(min_dist, distances[row][col])

        return min_dist


# works, but slow, don't pass. it starts from lands, not buildings.
# the optimized version starts from buildings. imo it is clean, i would probably
# do this in the interview if the interviewer don't say anything.
from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def neighbors(row, col):
            directions = {(row - 1, col), (row + 1, col),
                          (row, col - 1), (row, col + 1)}
            for r, c in directions:
                if (0 <= r < len(grid) and
                    0 <= c < len(grid[r]) and
                    grid[r][c] != 2):
                    yield r, c

        def bfs(row, col, total_buildings):
            queue = deque([(row, col, 0)])
            visited = {(row, col)}
            buildings_reached = total_dist = 0

            while queue:
                curr_r, curr_c, curr_dist = queue.popleft()
                for n_r, n_c in neighbors(curr_r, curr_c):
                    if (n_r, n_c) not in visited:
                        visited.add((n_r, n_c))
                        if grid[n_r][n_c] == 1:
                            buildings_reached += 1
                            total_dist += curr_dist + 1
                        else:
                            queue.append((n_r, n_c, 1 + curr_dist))

            if buildings_reached == total_buildings:
                return total_dist
            else:
                return float('inf')

        total_buildings = sum(r.count(1) for r in grid)
        dist = float('inf')

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dist = min(dist, bfs(i, j, total_buildings))

        return dist if dist != float('inf') else -1
