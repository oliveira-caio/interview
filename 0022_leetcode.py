"""22. Generate Parentheses

link: https://leetcode.com/problems/generate-parentheses/

problem: Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, output, comb):
            if right < left:
                return
            elif left == 0 and right == 0:
                output.append(''.join(comb))
            if left > 0:
                comb.append('(')
                backtrack(left - 1, right, output, comb)
                comb.pop()
            if right > 0:
                comb.append(')')
                backtrack(left, right - 1, output, comb)
                comb.pop()

        output = []
        backtrack(n, n, output, [])
        return output
