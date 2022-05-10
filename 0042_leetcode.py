"""42. Trapping Rain Water

link: https://leetcode.com/problems/trapping-rain-water/

problem: Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = max_so_far = max_left = 0
        max_right = {}

        for i in range(len(height) - 1, -1, -1):
            if height[i] > max_so_far:
                max_so_far = height[i]
            max_right[i] = max_so_far

        for i in range(len(height)):
            max_left = max(max_left, height[i])
            total_water += min(max_left, max_right[i]) - height[i]

        return total_water
