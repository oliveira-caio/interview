"""528. Random Pick with Weight

link: https://leetcode.com/problems/random-pick-with-weight/

problem: You are given a 0-indexed array of positive integers w where w[i]
describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in
the range [0, w.length - 1] (inclusive) and returns it. The probability of
picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is
1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is
3 / (1 + 3) = 0.75 (i.e., 75%).

Example 1:
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is
only one element in w.

Example 2:
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. Returns the second element (index = 1) that
has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. Returns the first element (index = 0) that
has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.

Constraints:
1 <= w.length <= 10^4
1 <= w[i] <= 10^5
pickIndex will be called at most 10^4 times.
"""


from random import randint


class Solution:

    def __init__(self, w: List[int]):
        self.accum = [w[0]]
        for i in range(1, len(w)):
            self.accum.append(self.accum[i - 1] + w[i])

    def pickIndex(self) -> int:
        rand = randint(0, self.accum[-1] - 1)
        left, right = 0, len(self.accum) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if rand < self.accum[0]:
                return 0
            elif mid > 0 and self.accum[mid - 1] <= rand < self.accum[mid]:
                return mid
            elif rand < self.accum[mid]:
                right = mid - 1
            else:
                left = mid + 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
