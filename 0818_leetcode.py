"""818. Race Car

link: https://leetcode.com/problems/race-car/

problem: Your car starts at position 0 and speed +1 on an infinite number line.
Your car can go into negative positions. Your car drives automatically according
to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

- When you get an instruction 'A', your car does the following:
--- position += speed
--- speed *= 2
- When you get an instruction 'R', your car does the following:
--- If your speed is positive then speed = -1
--- otherwise speed = 1
- Your position stays the same.

For example, after commands "AAR", your car goes to positions 0 -> 1 -> 3 -> 3,
and your speed goes to 1 -> 2 -> 4 -> -1.

Given a target position target, return the length of the shortest sequence of
instructions to get there.

Example 1:
Input: target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.

Example 2:
Input: target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.

Constraints:
1 <= target <= 10^4
"""


# the time/space complexity analysis: we are basically bounded by the size of
# visited in both cases, and visited keep track of the positions and the speeds.
# since the positions can be anything up to 2*target and the speeds can be
# ..., -8, -4, -2, -1, 1, 2, 4, 8, ..., we have O(2*target*2log_2(target)).
from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)]) # position, speed, shortest path
        visited = {(0, 1)} # position, speed

        while queue:
            curr_pos, curr_speed, curr_path = queue.popleft()

            if curr_pos == target:
                return curr_path

            # advance
            next_pos = curr_pos + curr_speed
            next_speed = 2*curr_speed
            next_path = curr_path + 1
            if ((next_pos, next_speed) not in visited and
                0 < next_pos and
                next_pos < 2*target):
                visited.add((next_pos, next_speed))
                queue.append((next_pos, next_speed, next_path))

            # return
            next_pos = curr_pos
            next_speed = -1 if curr_speed > 0 else 1
            next_path = curr_path + 1
            if ((next_pos, next_speed) not in visited and
                0 < next_pos and
                next_pos < 2*target):
                visited.add((next_pos, next_speed))
                queue.append((next_pos, next_speed, next_path))
