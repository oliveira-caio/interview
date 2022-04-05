"""
link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

problem: Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in
nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may
assume the returned list does not count as extra space.
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        nums = set(nums)
        res = []
        for i in range(1, size + 2):
            if i not in nums:
                res.append(i)
        return res


# follow up
class Solution:
    def setbit(self, n, bits):
        index = n >> 5
        bits[index] |= (1 << (n % 32))

    def getbit(self, n, bits):
        index = n >> 5
        return (bits[index] & (1 << (n % 32))) == 0

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        bits = [0 for _ in range(1 + (len(nums) >> 5))]
        res = []

        for n in nums:
            self.setbit(n, bits)
        
        for i in range(1, len(nums) + 1):
            if self.getbit(i, bits):
                res.append(i)

        return res
