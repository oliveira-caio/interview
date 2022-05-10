"""140. Word Break II

link: https://leetcode.com/problems/word-break-ii/

problem: Given a string s and a dictionary of strings wordDict, add spaces in s
to construct a sentence where each word is a valid dictionary word. Return all
such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine",
"pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:
1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


# top down dp, first thought
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dp(string, memo={}):
            if string in memo:
                return memo[string]
            elif string == '':
                return ['']

            memo[string] = []

            for word in wordDict:
                if string.find(word) == 0:
                    for x in dp(string[len(word):], memo):
                        memo[string].append((word + ' ' + x).strip())

            return memo[string]
        
        return dp(s)


# bottom up dp, second thought
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        table = [[] for _ in range(len(s) + 1)]
        table[0] = ['']

        for i in range(len(table)):
            if table[i]:
                for word in wordDict:
                    if s[i:].find(word) == 0:
                        for x in table[i]:
                            table[i + len(word)].append((x + ' ' + word).strip())

        return table[-1]
