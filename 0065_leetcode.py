"""65. Valid Number

link: https://leetcode.com/problems/valid-number/

problem: A valid number can be split up into these components (in order):
- A decimal number or an integer.
- (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
- (Optional) A sign character (either '+' or '-').
- One of the following formats:
--- One or more digits, followed by a dot '.'.
--- One or more digits, followed by a dot '.', followed by one or more digits.
--- A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
- (Optional) A sign character (either '+' or '-').
- One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14",
"4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while
the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6",
"-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false

Constraints:
1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9),
plus '+', minus '-', or dot '.'.
"""


# my stupid working solution
class Solution:
    def isNumber(self, s: str) -> bool:
        def is_integer(string):
            if len(string) == 0:
                return False
            if string.isdigit() or (string[0] in {'-', '+'}
                                    and string[1:].isdigit():)
                return True
            return False
        
        def is_decimal(string):
            if "." not in string:
                return is_integer(string)
            num = string.split('.')
            if len(num) > 2:
                return False
            if is_integer(num[0]) and num[1] == '':
                return True
            elif is_integer(num[0]) and num[1].isdigit():
                return True
            elif num[0] == '' and num[1].isdigit():
                return True
            elif num[0] == '-' and num[1].isdigit():
                return True
            elif num[0] == '+' and num[1].isdigit():
                return True
            return False
        
        num = []
        if 'e' not in s and 'E' not in s:
            return is_integer(s) or is_decimal(s)
        if 'e' in s and 'E' in s:
            return False
        if 'e' in s:
            num = s.split('e')
        if 'E' in s:
            num = s.split('E')
        if len(num) != 2:
            return False
        if not is_integer(num[1]):
            return False
        return is_integer(num[0]) or is_decimal(num[0])


# smart solution
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in {"+", "-"}:
                if i > 0 and s[i - 1] not in {"e", "E"}:
                    return False
            elif c in {"e", "E"}:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit


class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_sign = seen_exp = seen_dot = False

        for c in s:
            if c.isdigit():
                seen_digit = True
            elif c in {'+', '-'}:
                if seen_digit or seen_sign or (seen_dot and not seen_exp):
                    return False
                seen_sign = True
            elif c in {'e', 'E'}:
                if not seen_digit or seen_exp:
                    return False
                seen_exp = True
                seen_digit = False
                seen_sign = False
            elif c == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit
