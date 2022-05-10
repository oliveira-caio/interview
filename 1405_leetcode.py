"""1405. Longest Happy String

link: https://leetcode.com/problems/longest-happy-string/

problem: A string s is called happy if it satisfies the following conditions:

- s only contains the letters 'a', 'b', and 'c'.
- s does not contain any of "aaa", "bbb", or "ccc" as a substring.
- s contains at most a occurrences of the letter 'a'.
- s contains at most b occurrences of the letter 'b'.
- s contains at most c occurrences of the letter 'c'.

Given three integers a, b, and c, return the longest possible happy string. If
there are multiple longest happy strings, return any of them. If there is no
such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

Constraints:
0 <= a, b, c <= 100
a + b + c > 0
"""


from heapq import *


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []; result = []

        for count, letter in {(-a, 'a'), (-b, 'b'), (-c, 'c')}:
            if count:
                heappush(max_heap, (count, letter))

        while max_heap:
            count, letter = heappop(max_heap)

            if len(result) >= 2 and result[-1] == result[-2] == letter:
                if not max_heap:
                    break
                else:
                    count, letter = heapreplace(max_heap, (count, letter))

            result.append(letter)
            if count + 1:
                heappush(max_heap, (count + 1, letter))

        return ''.join(result)
