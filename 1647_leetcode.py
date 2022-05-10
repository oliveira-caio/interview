"""1647. Minimum Deletions to Make Character Frequencies Unique

link: https://bit.ly/3FADffG

problem: A string s is called good if there are no two different characters in s
that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to
make s good.

The frequency of a character in a string is the number of times it appears in
the string. For example, in the string "aab", the frequency of 'a' is 2, while
the frequency of 'b' is 1.

Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string
"aaabbc".

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end
(i.e. frequency of 0 is ignored).

Constraints:
1 <= s.length <= 10^5
s contains only lowercase English letters.
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        freq_inv = {i: [] for i in range(len(s) + 1)}
        res = 0

        for c in s:
            freq[c] = 1 + freq.get(c, 0)

        for k, v in freq.items():
            freq_inv[v].append(k)

        for k, v in freq_inv.items():
            if len(v) != 1:
                for i in range(len(v) - 1):
                    freq_c = k
                    while freq_c > 0 and len(freq_inv[freq_c]) >= 1:
                        freq_c -= 1; res += 1
                    freq_inv[freq_c].append(v[i])

        return res
