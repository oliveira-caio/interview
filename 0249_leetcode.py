"""249. Group Shifted Strings

link: https://leetcode.com/problems/group-shifted-strings/

problem: We can shift a string by shifting each of its letters to its successive
letter.

- For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

- For example, we can keep shifting "abc" to form the sequence:
"abc" -> "bcd" -> ... -> "xyz".

Given an array of strings strings, group all strings[i] that belong to the same
shifting sequence. You may return the answer in any order.

Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
Input: strings = ["a"]
Output: [["a"]]

Constraints:
1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""


# my first solution, a little slow but passed
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def is_shift(s_one, s_two):
            min_val, max_val = ord('a'), ord('z')
            for i in range(1, 27):
                temp = []
                for c in s_one:
                    if ord(c) + i > max_val:
                        temp.append(chr(min_val - 1 + (ord(c) + i - max_val)))
                    else:
                        temp.append(chr(ord(c) + i))
                if s_two == ''.join(temp):
                    return True
            return False
            
        shifts = {}
        for string in strings:
            flag = False
            for key in shifts:
                if is_shift(string, key):
                    shifts[key].append(string)
                    flag = True
            if not flag:
                shifts[string] = [string]
        return shifts.values()


# saw the idea elsewhere, but implemented myself.
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shifts = {}
        for string in strings:
            key = [0]
            for i in range(1, len(string)):
                key.append((ord(string[i]) - ord(string[i - 1])) % 26)
            key = tuple(key)
            if key in shifts:
                shifts[key].append(string)
            else:
                shifts[key] = [string]
        return shifts.values()
