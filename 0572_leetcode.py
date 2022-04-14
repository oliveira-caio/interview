"""572. Subtree of Another Tree

link: https://leetcode.com/problems/subtree-of-another-tree/

problem: ven the roots of two binary trees root and subRoot, return true if
there is a subtree of root with the same structure and node values of subRoot
and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and
all of this node's descendants. The tree tree could also be considered as a
subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self,
                  root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:
        def check(node_one, node_two):
            if not node_one and not node_two:
                return True
            elif not node_one and node_two:
                return False
            elif node_one and not node_two:
                return False
            elif node_one.val != node_two.val:
                return False
            elif not check(node_one.left, node_two.left):
                return False
            elif not check(node_one.right, node_two.right):
                return False
            return True
        
        def dfs(node):
            if not node:
                return False
            return check(node, subRoot) or dfs(node.left) or dfs(node.right)
            
        return dfs(root)


# had done this exercise previously, but didn't remember the smart solution. the
# above is the naive version. the smart uses the fact that traversing a three in
# preorder gives a unique representation of the tree, then we can just use this
# representation and check if one string is a substring of the other.
class Solution:
    def isSubtree(self,
                  root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:
        def preorder(node):
            if not node:
                return "[x]"
            str_repr = "[" + str(node.val) "]"
            str_repr += preorder(node.left)
            str_repr += preorder(node.right)
            return str_repr

        big_tree = preorder(root)
        small_tree = preorder(subRoot)

        return small_tree in big_tree
