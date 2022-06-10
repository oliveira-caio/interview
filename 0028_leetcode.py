"""28. Implement strStr()

link: https://leetcode.com/problems/implement-strstr/

problem: Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        i = j = 0

        while j < len(haystack):
            if needle[i] == haystack[j]:
                k = j
                while (i < len(needle) and
                       k < len(haystack) and
                       needle[i] == haystack[k]):
                    i += 1; k += 1
                if i == len(needle):
                    return j
                else:
                    i = 0
            j += 1

        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i : i + len(needle)]:
                return i

            return -1


from collections import deque


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        hashed_needle = hash(needle)
        window = deque(haystack[:len(needle)])

        for i in range(len(needle), len(haystack) + 1):
            hashed_window = hash(''.join(window))
            if hashed_needle == hashed_window:
                return i - len(needle)
            window.popleft()
            if i < len(haystack):
                window.append(haystack[i])

        return -1
