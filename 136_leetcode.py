"""
link: https://leetcode.com/problems/single-number/

problem: Given a non-empty array of integers nums, every element appears twice
except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears
only once.
"""


class Solution:
    def setbit(self, n, bits):
        index = n >> 5
        bits[index] ^= 1 << (n % 32)
    
    def getbit(self, n, bits):
        index = n >> 5
        return (bits[index] & (1 << (n % 32))) == 0
    
    def singleNumber(self, nums: List[int]) -> int:
        max_val = max(nums) # or 1 + (30000 >> 5)
        min_val = -min(nums) # or 1 + (30000 >> 5)
        bits_pos = [0 for _ in range(1 + (max_val >> 5))]
        bits_neg = [0 for _ in range(1 + (min_val >> 5))]
        
        for n in nums:
            if n >= 0:
                self.setbit(n, bits_pos)
            else:
                self.setbit(-n, bits_neg)
        
        for n in nums:
            if n >= 0 and not self.getbit(n, bits_pos):
                return n
            elif n < 0 and not self.getbit(-n, bits_neg):
                return n
