"""539. Minimum Time Difference

link: https://leetcode.com/problems/minimum-time-difference/

problem: Given a list of 24-hour clock time points in "HH:MM" format, return the
minimum minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints.length <= 2 * 10^4
timePoints[i] is in the format "HH:MM".
"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(time):
            h, m = map(int, time.split(':'))
            return 60*h + m

        minutes = sorted(map(convert_to_minutes, timePoints))
        minutes.append(24*60 + minutes[0])
        return min(b - a for a, b in zip(minutes, minutes[1:]))
