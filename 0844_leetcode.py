"""844. Backspace String Compare

link: https://leetcode.com/problems/backspace-string-compare/

problem: Given two strings s and t, return true if they are equal when both are
typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def listify(string):
            list_str = []
            for c in string:
                if c != '#':
                    list_str.append(c)
                elif list_str:
                    list_str.pop()
            return list_str
        return listify(s) == listify(t)
