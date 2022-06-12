"""90. Subsets II

link: https://leetcode.com/problems/subsets-ii/

problem: Given an integer array nums that may contain duplicates, return all
possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any
order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(arr):
            if len(arr) == 0:
                return {()}
            first = arr[0]
            rest = helper(arr[1:])
            return rest.union({tuple([first] + list(x)) for x in rest})

        return helper(sorted(nums))
