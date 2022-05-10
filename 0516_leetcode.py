"""516. Longest Palindromic Subsequence

link: https://leetcode.com/problems/longest-palindromic-subsequence/

problem: Given a string s, find the longest palindromic subsequence's length in
s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dp(l, r, memo={}):
            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                memo[(l, r)] = 2 + dp(l + 1, r - 1, memo)
            else:
                memo[(l, r)] = max(dp(l + 1, r, memo), dp(l, r - 1, memo))

            return memo[(l, r)]

        return dp(0, len(s) - 1)
