"""227. Basic Calculator II

link: https://leetcode.com/problems/basic-calculator-ii/

problem: Given a string s which represents an expression, evaluate this
expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate
results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
- 1 <= s.length <= 3 * 105
- s consists of integers and operators ('+', '-', '*', '/') separated by some
number of spaces.
- s represents a valid expression.
- All the integers in the expression are non-negative integers in the range
[0, 2^31 - 1].
- The answer is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def calculate(self, s: str) -> int:
        curr_number = last_number = result = 0
        sign = '+'

        for i, c in enumerate(s):
            if c.isdigit():
                curr_number = 10*curr_number + int(c)

            if i == len(s) - 1 or c in {'+', '-', '*', '/'}:
                if sign == '+':
                    result += last_number
                    last_number = curr_number
                elif sign == '-':
                    result += last_number
                    last_number = -curr_number
                elif sign == '*':
                    last_number = last_number * curr_number
                else:
                    if last_number < 0:
                        last_number = -((-last_number) // curr_number)
                    else:
                        last_number = last_number // curr_number
                sign = c; curr_number = 0

        return result + last_number
