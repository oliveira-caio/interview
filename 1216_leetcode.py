"""1216. Valid Palindrome III

link: https://leetcode.com/problems/valid-palindrome-iii/

problem: Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing
at most k characters from it.

Example 1:
Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.

Example 2:
Input: s = "abbababa", k = 1
Output: true

Constraints:
1 <= s.length <= 1000
s consists of only lowercase English letters.
1 <= k <= s.length
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
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

        return True if dp(0, len(s) - 1) >= len(s) - k else False
