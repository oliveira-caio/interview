"""169. Majority Element

link: https://leetcode.com/problems/majority-element/

problem: Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You
may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for k in freq:
            if freq[k] > len(nums) // 2:
                return k


# follow up (this is boyer-moore voting algorithm):
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
