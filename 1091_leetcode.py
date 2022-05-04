from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row, max_col = len(grid) - 1, len(grid[0]) - 1

        def neighbors(row, col):
            directions = {(row - 1, col - 1), (row - 1, col),
                          (row - 1, col + 1), (row, col - 1),
                          (row, col + 1), (row + 1, col - 1),
                          (row + 1, col), (row + 1, col + 1)}
            for r, c in directions:
                if 0 <= r <= max_row and 0 <= c <= max_col and grid[r][c] == 0:
                    yield r, c

        if grid[0][0] == 1 or grid[max_row][max_col] == 1:
            return -1

        queue = deque()
        queue.append((0, 0, 1)) # row, col, distance
        visited = {(0, 0)}

        while queue:
            row, col, distance = queue.popleft()
            if row, col == max_row, max_col:
                return distance
            for neighbor in neighbors(row, col):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((*neighbor, distance + 1))

        return -1
