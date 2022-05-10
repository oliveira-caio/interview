"""224. Basic Calculator

link: https://leetcode.com/problems/basic-calculator/

problem: Given a string s representing a valid expression, implement a basic
calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""


# sometimes it pass, sometimes not.
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def evaluate(expression):
            result = last_number = curr_number = 0
            sign = '+'
            seen_nonzero = prev_zero = False

            for i, c in enumerate(expression):
                if c.isdigit():
                    if seen_nonzero is False and prev_zero is True:
                        return False
                    if c != '0':
                        seen_nonzero = True
                    else:
                        prev_zero = True
                    curr_number = 10*curr_number + int(c)

                if i == len(expression) - 1 or c in {'+', '-', '*'}:
                    if sign == '+':
                        result += last_number
                        last_number = curr_number
                    elif sign == '-':
                        result += last_number
                        last_number = -curr_number
                    else:
                        last_number = last_number * curr_number
                    prev_zero = seen_nonzero = False
                    curr_number = 0
                    sign = c

            return result + last_number == target

        candidates = {num: 1}
        output = set()

        while candidates:
            output.update(filter(evaluate, candidates))

            for candidate, index in list(candidates.items()):
                if index >= len(candidate):
                    candidates.pop(candidate)
                else:
                    first, second = candidate[:index], candidate[index:]
                    candidates[first + '+' + second] = index + 2
                    candidates[first + '*' + second] = index + 2
                    candidates[first + '-' + second] = index + 2
                    candidates[candidate] = index + 1

        return output
