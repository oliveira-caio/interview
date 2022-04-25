"""314. Binary Tree Vertical Order Traversal

link: https://leetcode.com/problems/binary-tree-vertical-order-traversal/

problem: Given the root of a binary tree, return the vertical order traversal of
its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to
right.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

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
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def leftmost(node):
            if not node:
                return -1
            left = leftmost(node.left) + 1
            right = leftmost(node.right) - 1
            return max(left, right)
        
        def rightmost(node):
            if not node:
                return -1
            left = rightmost(node.left) - 1
            right = rightmost(node.right) + 1
            return max(left, right)
        
        def bfs(index, result):
            if not root:
                return
            queue = deque()
            queue.append((root, index))
            while queue:
                curr_node, curr_index = queue.popleft()
                result[curr_index].append(curr_node.val)
                if curr_node.left:
                    queue.append((curr_node.left, curr_index - 1))
                if curr_node.right:
                    queue.append((curr_node.right, curr_index + 1))
                
        left = leftmost(root)
        right = rightmost(root)
        result = [[] for _ in range(right + left + 1)]
        bfs(left, result)
        return result
