"""76. Minimum Window Substring

link: https://leetcode.com/problems/minimum-window-substring/

problem: Given two strings s and t of lengths m and n respectively, return the
minimum window substring of s such that every character in t (including
duplicates) is included in the window. If there is no such substring, return
the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from
string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        freq_window = {c: 0 for c in s}
        freq_t = {}
        left, right = 0, 0
        min_window = ''

        for c in t:
            freq_t[c] = 1 + freq_t.get(c, 0)

        freq_window[s[0]] = 1
        while right < len(s):
            flag = True
            for c in freq_t:
                if c not in freq_window or freq_t[c] > freq_window[c]:
                    flag = False
                    break
            if flag:
                if not min_window or right - left + 1 < len(min_window):
                    min_window = s[left : right + 1]
                freq_window[s[left]] -= 1
                left += 1
            else:
                right += 1
                if right < len(s):
                    freq_window[s[right]] += 1

        return min_window
