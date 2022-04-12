"""53. Maximum Subarray

link: https://leetcode.com/problems/maximum-subarray/

problem: Given an integer array nums, find the contiguous subarray (containing
at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        max_at = 0
        for n in nums:
            max_at = max(max_at + n, n)
            res = max(res, max_at)
        return res

# the follow up can be found in programming pearls, page 79. the solution is
# O(nlog(n)), so i won't bother, but the idea is to divide the vector in half
# recursively and then find a way to concatenate the maximum subarray of
# both halves. this concatenation is the tricky part.
