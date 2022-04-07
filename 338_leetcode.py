"""
link: https://leetcode.com/problems/counting-bits/

problem: Given an integer n, return an array ans of length n + 1 such that for
each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation
of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101 

Constraints:
0 <= n <= 10^5

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            while i != 0:
                if 1 & i == 1:
                    count += 1
                i = i >> 1
            ans.append(count)
        return ans


"""
follow up

explanation: if a number x is odd, then the number of 1's in its bin repr is
1 + (number of 1's in the bin repr of x // 2). if a number is even, then
the it is equal to the number of 1's in the bin repr of x // 2.

examples:
x = 7, then its bin repr is 111 and the bin repr of 3 is 11
x = 12, then its bin repr is 1100 and the bin repr of 6 is 110
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            if i % 2 == 0:
                ans.append(ans[i >> 1])
            else:
                ans.append(1 + ans[i >> 1])
        return ans
