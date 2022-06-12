"""46. Permutations

link: https://leetcode.com/problems/permutations/

problem: Given an array nums of distinct integers, return all the possible
permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        first = [nums[0]]
        rest = self.permute(nums[1:])
        perms = []
        for perm in rest:
            for i in range(len(perm) + 1):
                perms.append(perm[:i] + first + perm[i:])
        return perms


import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_index, output):
            if curr_index == len(nums):
                output.append(nums.copy())
                return
            for i in range(curr_index, len(nums)):
                nums[i], nums[curr_index] = nums[curr_index], nums[i]
                backtrack(curr_index + 1, output)
                nums[i], nums[curr_index] = nums[curr_index], nums[i]
        
        output = []
        backtrack(0, output)
        return output
