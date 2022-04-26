"""560. Subarray Sum Equals K

link: https://leetcode.com/problems/subarray-sum-equals-k/

problem: Given an array of integers nums and an integer k, return the total
number of subarrays whose sum equals to k.

Example 1:
input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        result = curr_sum = 0
        for n in nums:
            curr_sum += n
            if curr_sum - k in prefix_sum:
                result += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] = 1 + prefix_sum.get(curr_sum, 0)
        return result
