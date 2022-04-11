"""
link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

problem: Given the root of a binary tree, return the average value of the nodes
on each level in the form of an array. Answers within 10^-5 of the actual answer
will be accepted.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def bfs():
            result = {}
            stack = [(root, 0)]
            while stack:
                curr, level = stack.pop()
                if level not in result:
                    result[level] = [0, 0]
                result[level][0] += curr.val
                result[level][1] += 1
                if curr.left:
                    stack.append((curr.left, 1 + level))
                if curr.right:
                    stack.append((curr.right, 1 + level))
            return result
        return [v[0] / v[1] for v in bfs().values()]
