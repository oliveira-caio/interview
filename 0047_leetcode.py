"""47. Permutations II

link: https://leetcode.com/problems/permutations-ii/

problem: Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        first = [nums[0]]
        rest = self.permuteUnique(nums[1:])
        perms = set()
        for perm in rest:
            for i in range(len(perm) + 1):
                list_perm = list(perm)
                perms.add(tuple(list_perm[:i] + first + list_perm[i:]))
        return perms
