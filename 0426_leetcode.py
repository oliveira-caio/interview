"""426. Convert Binary Search Tree to Sorted Doubly Linked List

link: bit.ly/3KlyUgW

problem: Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in
place.

You can think of the left and right pointers as synonymous to the predecessor
and successor pointers in a doubly-linked list. For a circular doubly linked
list, the predecessor of the first element is the last element, and the
successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left
pointer of the tree node should point to its predecessor, and the right pointer
should point to its successor. You should return the pointer to the smallest
element of the linked list.

Example 1:
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
Explanation: The figure below shows the transformed BST. The solid line
indicates the successor relationship, while the dashed line means the
predecessor relationship.

Example 2:
Input: root = [2,1,3]
Output: [1,2,3]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# faster
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def in_order(node, serialize):
            if node:
                in_order(node.left, serialize)
                serialize.append(node)
                in_order(node.right, serialize)

        if not root:
            return None

        serialize = []
        in_order(root, serialize)

        serialize[0].left = serialize[-1]
        serialize[-1].right = serialize[0]
        if len(serialize) > 1:
            serialize[0].right = serialize[1]
            serialize[-1].left = serialize[-2]
        for i in range(1, len(serialize) - 1):
            serialize[i].left = serialize[i - 1]
            serialize[i].right = serialize[i + 1]

        return serialize[0]


# cleaner
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def in_order(node, serialize):
            if node:
                in_order(node.left, serialize)
                serialize.append(node)
                in_order(node.right, serialize)

        if not root:
            return None

        serialize = []
        in_order(root, serialize)

        for i in range(len(serialize)):
            if i - 1 >= 0:
                serialize[i].left = serialize[i - 1]
            else:
                serialize[0].left = serialize[-1]
            if i + 1 < len(serialize):
                serialize[i].right = serialize[i + 1]
            else:
                serialize[-1].right = serialize[0]

        return serialize[0]

