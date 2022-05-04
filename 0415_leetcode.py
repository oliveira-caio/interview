"""415. Add Strings

link: https://leetcode.com/problems/add-strings/

problem: Given two non-negative integers, num1 and num2 represented as string,
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large
integers (such as BigInteger). You must also not convert the inputs to integers
directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
1 <= num1.length, num2.length <= 10^4
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        map_to_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        map_to_string = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                         5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        curr_sum = []
        carry = False
        first, second = len(num1) - 1, len(num2) - 1
        while first >= 0 or second >= 0:
            n_one = '0' if first < 0 else num1[first]
            n_two = '0' if second < 0 else num2[second]
            _sum = map_to_digit[n_one] + map_to_digit[n_two]
            if carry:
                _sum += 1
            carry = True if _sum > 9 else False
            curr_sum.append(map_to_string[_sum % 10])
            first -= 1; second -= 1
        if carry:
            curr_sum.append('1')
        return ''.join(reversed(curr_sum))
