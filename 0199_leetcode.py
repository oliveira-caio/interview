"""199. Binary Tree Right Side View

link: https://leetcode.com/problems/binary-tree-right-side-view/

problem: Given the root of a binary tree, imagine yourself standing on the
right side of it. Return the values of the nodes you can see ordered from top
to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodes = {}
        queue = deque()
        queue.append((0, root))
        while queue:
            row, node = queue.popleft()
            if row in nodes:
                nodes[row].append(node.val)
            else:
                nodes[row] = [node.val]
            if node.left:
                queue.append((row + 1, node.left))
            if node.right:
                queue.append((row + 1, node.right))
        return [v[-1] for v in nodes.values()]
