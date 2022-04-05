"""
link: https://leetcode.com/problems/climbing-stairs/

problem: You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        num_ways = [0 for _ in range(n + 2)]
        num_ways[0] = 1

        for i in range(n):
            num_ways[i + 1] += num_ways[i]
            num_ways[i + 2] += num_ways[i]

        return num_ways[-2]


# alternative
class Solution:
    def dp(self, n, memo):
        if n in memo:
            return memo[n]
        if n < 2:
            return 1
        memo[n] = self.dp(n - 1, memo) + self.dp(n - 2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        return self.dp(n, {})
