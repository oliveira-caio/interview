"""125. Valid Palindrome

link: https://leetcode.com/problems/valid-palindrome/

problem: A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(converted) - 1
        
        while left < right:
            if converted[left] != converted[right]:
                return False
            left += 1; right -= 1
            
        return True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(target, memo={}):
            if target in memo:
                return memo[target]
            elif target == '':
                return True
            
            for word in wordDict:
                if target.find(word) == 0 and dp(target[len(word):], memo):
                    memo[target] = True
                    return True
            
            memo[target] = False
            return memo[target]
        
        return dp(s)
