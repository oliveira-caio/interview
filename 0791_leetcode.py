"""791. Custom Sort String

link: https://leetcode.com/problems/custom-sort-string/

problem: You are given two strings order and s. All the words of order are
unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted.
More specifically, if a character x occurs before a character y in order, then x
should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b",
and "a". 
Since "d" does not appear in order, it can be at any position in the returned
string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:
Input: order = "cbafg", s = "abcd"
Output: "cbad"

Constraints:
1 <= order.length <= 26
1 <= s.length <= 200
order and s consist of lowercase English letters.
All the characters of order are unique.
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def mergesort(string):
            if len(string) < 2:
                return string
            middle = len(string) // 2
            less_in_order = set()
            less, greater, equal = [], [], []
            if string[middle] in order:
                for c in order:
                    if c != string[middle]:
                        less_in_order.add(c)
                    else:
                        break
            for c in string:
                if c == string[middle]:
                    equal.append(c)
                elif c in less_in_order:
                    less.append(c)
                else:
                    greater.append(c)
            less = ''.join(less)
            greater = ''.join(greater)
            equal = ''.join(equal)
            return mergesort(less) + equal + mergesort(greater)
        return mergesort(s)
