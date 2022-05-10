"""301. Remove Invalid Parentheses

link: https://leetcode.com/problems/remove-invalid-parentheses/

problem: Given a string s that contains parentheses and letters, remove the
minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]

Constraints:
1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""


# the beautiful solution by stefan pochmann
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check_pars(string):
            counter = 0
            for c in string:
                if c == '(':
                    counter += 1
                elif c == ')':
                    counter -= 1
                    if counter < 0:
                        return False
            return counter == 0

        candidates = {s}
        while True:
            result = list(filter(check_pars, candidates))

            if result:
                return result

            candidates = {candidate[:i] + candidate[i+1:]
                          for candidate in candidates
                          for i in range(len(candidate))}


# my attempt. too slow, but works.
from copy import deepcopy


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check_pars(string):
            if string.count('(') != string.count(')'):
                return False

            stack = []
            for c in string:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if not stack:
                        return False
                    stack.pop()

            return True

        def generate_tuples(possible, n, previous):
            if n == 1:
                return [[x] for x in possible]

            result = []
            for p in possible:
                for t in previous:
                    if p < t[-1]:
                        result.append(t + [p])

            return result

        if check_pars(s):
            return [s]

        result = set()
        possible = [i for i, c in enumerate(s) if c in {'(', ')'}]
        count_pars = len(possible)
        prev = None

        for i in range(1, count_pars + 1):
            all_tuples = generate_tuples(possible, i, prev)
            prev = copy.deepcopy(all_tuples)
            flag = False
            for t in all_tuples:
                t = set(t)
                candidate = [c for i, c in enumerate(s) if i not in t]
                if check_pars(candidate):
                    flag = True
                    result.add(''.join(candidate))
            if flag:
                return result

        return [""]
