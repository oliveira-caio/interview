"""1650. Lowest Common Ancestor of a Binary Tree III

link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

problem: Given two nodes of a binary tree p and q, return their lowest common
ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is
below:

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

According to the definition of LCA on Wikipedia: "The lowest common ancestor of
two nodes p and q in a tree T is the lowest node that has both p and q as
descendants (where we allow a node to be a descendant of itself)."

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of
itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q exist in the tree.
"""


# my original solution:
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = set()
        node = p
        while node:
            parents.add(node)
            node = node.parent
        node = q
        while node:
            if node in parents:
                return node
            node = node.parent


# clever solution, it also works for intersection of linked lists.
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        node_one, node_two = p, q
        while node_one != node_two:
            node_one = node_one.parent if node_one.parent else q
            node_two = node_two.parent if node_two.parent else p
        return node_one
