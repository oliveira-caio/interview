"""977. Squares of a Sorted Array

link: https://leetcode.com/problems/squares-of-a-sorted-array/

problem: Given an integer array nums sorted in non-decreasing order, return an
array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg_squared = list(reversed([x * x for x in nums if x < 0]))
        pos_squared = [x * x for x in nums if x >= 0]
        ans = []; i = j = 0
        while i < len(neg_squared) or j < len(pos_squared):
            neg = float('inf') if i == len(neg_squared) else neg_squared[i]
            pos = float('inf') if j == len(pos_squared) else pos_squared[j]
            if neg < pos:
                ans.append(neg); i += 1
            else:
                ans.append(pos); j += 1
        return ans
