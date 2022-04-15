"""287. Find the Duplicate Number

link: https://leetcode.com/problems/find-the-duplicate-number/

problem: Given an array of integers nums containing n + 1 integers where each
integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only
constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which
appears two or more times.
"""


class Solution:
    def setbit(self, bits, n):
        index = n >> 5
        bits[index] ^= (1 << (n % 32))

    def getbit(self, bits, n):
        index = n >> 5
        return (bits[index] & (1 << (n % 32))) == 0

    def findDuplicate(self, nums: List[int]) -> int:
        bits = [0 for _ in range(1 + (len(nums) >> 5))]

        for n in nums:
            self.setbit(bits, n)
            if self.getbit(bits, n):
                return n


# follow up (it's basically a modificaption of the algorithm to find the first
# element of a cycle. having two equal numbers and this configuration apparently
# guarantees that there will be a cycle in the list. highly non-trivial,
# definitely would never think about that):
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
