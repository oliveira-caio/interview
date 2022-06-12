"""40. Combination Sum II

link: https://leetcode.com/problems/combination-sum-ii/

problem: Given a collection of candidate numbers (candidates) and a target
number (target), find all unique combinations in candidates where the candidate
numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


from collections import Counter
import copy


class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(curr_target, start, curr_comb, counter, output):
            if curr_target == 0:
                output.append(curr_comb.copy())
                return
            elif curr_target < 0:
                return
            else:
                for i in range(start, len(counter)):
                    candidate, freq = counter[i]
                    if freq <= 0:
                        continue
                    curr_comb.append(candidate)
                    counter[i] = (candidate, freq - 1)
                    backtrack(curr_target, i, curr_comb, counter, output)
                    curr_comb.pop()
                    counter[i] = (candidate, freq)

        output = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        backtrack(target, 0, [], counter, output)
        return output
