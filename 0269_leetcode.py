"""269. Alien Dictionary

link: https://leetcode.com/problems/alien-dictionary/

problem: There is a new alien language that uses the English alphabet. However,
the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary,
where the strings in words are sorted lexicographically by the rules of this new
language.

Return a string of the unique letters in the new alien language sorted in
lexicographically increasing order by the new language's rules. If there is no
solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter
where they differ, the letter in s comes before the letter in t in the alien
language. If the first min(s.length, t.length) letters are the same, then s is
smaller if and only if s.length < t.length.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""


from collections import deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def bfs(graph, source, output):
            queue = deque([source])
            visited = {source}

            while queue:
                curr = queue.popleft()
                output.append(curr)
                for neighbor in graph[curr][1]:
                    if neighbor not in visited:
                        graph[neighbor][0] -= 1
                        if graph[neighbor][0] == 0:
                            visited.add(neighbor)
                            queue.append(neighbor)

        def lexicographic(first, second):
            left, right = 0, 0

            while left < len(first) and right < len(second):
                if first[left] != second[right]:
                    return True, first[left], second[right]
                left += 1; right += 1

            if right == len(second) and left < len(first):
                return False, False, False

            return True, '', ''

        graph = {}
        start, output = [], []

        for word in words:
            for letter in word:
                if letter not in graph:
                    graph[letter] = [0, []]

        for i in range(len(words) - 1):
            valid, first, second = lexicographic(words[i], words[i + 1])
            if not valid:
                return ''
            if valid and first != '':
                graph[first][1].append(second)
                graph[second][0] += 1

        for letter in graph:
            if graph[letter][0] == 0:
                start.append(letter)

        for letter in start:
            bfs(graph, letter, output)

        return '' if len(output) != len(graph) else ''.join(output)
