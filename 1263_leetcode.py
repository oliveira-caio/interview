"""1263. Minimum Moves to Move a Box to Their Target Location

link: leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location

problem: Submissions
1263. Minimum Moves to Move a Box to Their Target Location
Hard

A storekeeper is a game in which the player pushes boxes around in a warehouse
trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element
is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following
rules:

- The character 'S' represents the player. The player can move up, down, left,
right in grid if it is a floor (empty cell).
- The character '.' represents the floor which means a free cell to walk.
- The character '#' represents the wall which means an obstacle (impossible to
walk there).
- There is only one box 'B' and one target cell 'T' in the grid.
- The box can be moved to an adjacent free cell by standing next to the box and
then moving in the direction of the box. This is a push.
- The player cannot walk through the box.

Return the minimum number of pushes to move the box to the target. If there is
no way to reach the target, return -1.

Example 1:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.

Example 2:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1

Example 3:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation: push the box down, left, left, up and up.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid contains only characters '.', '#', 'S', 'T', or 'B'.
There is only one character 'S', 'B', and 'T' in the grid.
"""


from collections import deque


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def valid(r, c):
            return (0 <= r < len(grid) and
                    0 <= c < len(grid[0]) and
                    grid[r][c] != '#')

        def check(curr, dest, box):
            queue = deque([curr])
            visited = set()

            while queue:
                r, c = queue.popleft()
                if (r, c) == dest:
                    return True
                new_pos = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in new_pos:
                    if (valid(nr, nc) and
                        (nr, nc) not in visited and
                        (nr, nc) != box):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'T':
                    target = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'S':
                    player = (i, j)

        queue = deque([(0, box, player)])
        visited = {(box, player)}

        while queue:
            n_pushes, box, player = queue.popleft()
            if box == target:
                return n_pushes
            b_coord = [(box[0] + 1, box[1]), (box[0] - 1, box[1]),
                       (box[0], box[1] + 1), (box[0], box[1] - 1)]
            p_coord = [(box[0] - 1, box[1]), (box[0] + 1, box[1]),
                       (box[0], box[1] - 1), (box[0], box[1] + 1)]
            for new_box, new_player in zip(b_coord, p_coord):
                if valid(*new_box) and (new_box, box) not in visited:
                    if valid(*new_player) and check(player, new_player, box):
                        visited.add((new_box, box))
                        queue.append((n_pushes + 1, new_box, box))

        return -1
