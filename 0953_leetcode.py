"""953. Verifying an Alien Dictionary

link: https://leetcode.com/problems/verifying-an-alien-dictionary/

problem: In an alien language, surprisingly, they also use English lowercase
letters, but possibly in a different order. The order of the alphabet is some
permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted
lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is
sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is
shorter (in size.) According to lexicographical rules "apple" > "app", because
'l' > '∅', where '∅' is defined as the blank character which is less than any
other character (More info).

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def check_words(word_one, word_two, dict_order):
            i = 0
            while i < min(len(word_one), len(word_two)):
                if dict_order[word_one[i]] < dict_order[word_two[i]]:
                    return True
                elif dict_order[word_one[i]] > dict_order[word_two[i]]:
                    return False
                i += 1
            return True if i == len(word_one) else False
        
        dict_order = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            if not check_words(words[i], words[i + 1], dict_order):
                return False
        return True
