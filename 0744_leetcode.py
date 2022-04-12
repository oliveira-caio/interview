"""744. Find Smallest Letter Greater Than Target

link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

problem: Given a characters array letters that is sorted in non-decreasing order
and a character target, return the smallest character in the array that is
larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example 3:
Input: letters = ["c","f","j"], target = "d"
Output: "f"

Constraints:
2 <= letters.length <= 10^4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""


### IMPORTANT: REMEMBER WHEN THERE ARE 3 OR MORE ELEMENTS WITH THE SAME VALUE.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if letters[middle] == target:
                while middle + 1 < len(letters): # find next different letter
                    if letters[middle + 1] != target:
                        return letters[middle + 1]
                    middle += 1
                return letters[0] # wrap around if doesn't find to the right
            elif target < letters[middle]:
                right = middle - 1
            else:
                left = middle + 1

        if target < letters[middle]:
            return letters[middle]

        while middle + 1 < len(letters): # find next different letter
            if letters[middle + 1] != target:
                return letters[middle + 1]
            middle += 1

        return letters[0] # wrap around if doesn't find to the right
