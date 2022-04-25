"""680. Valid Palindrome II

link: https://leetcode.com/problems/valid-palindrome-ii/

problem: Given a string s, return true if the s can be palindrome after deleting
at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1; right -= 1
            return True
        left = 0; right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return check(left + 1, right) or check(left, right - 1)
            left += 1; right -= 1
        return True
