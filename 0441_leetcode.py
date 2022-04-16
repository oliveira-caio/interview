"""442. Find All Duplicates in an Array

link: https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/

problem: Given an integer array nums of length n where all the integers of nums
are in the range [1, n] and each integer appears once or twice, return an array
of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra
space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""


# constant memory (would never thought about that, specially because i usually
# don't think about changing the input):
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                ans.append(index + 1)
            else:
                nums[index] = -nums[index]
        return ans


# what i would have done in a hurry:
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        return [k for k, v in freq.items() if v > 1]


# what i would have done with space constraint, though it is O(n / 32)
# strangely enough, this consumed less memory than the constant algorithm:
class Solution:
    def setbit(self, bits, n):
        index = n >> 5
        bits[index] ^= (1 << (n % 32))
        
    def getbit(self, bits, n):
        index = n >> 5
        return (bits[index] & (1 << (n % 32))) == 0
    
    def findDuplicates(self, nums: List[int]) -> List[int]:
        bits = [0 for _ in range(1 + (len(nums) >> 5))]
        ans = []
        for num in nums:
            if not self.getbit(bits, num):
                ans.append(num)
            self.setbit(bits, num)
        return ans
