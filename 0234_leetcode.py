"""234. Palindrome Linked List

link: https://leetcode.com/problems/palindrome-linked-list/

problem: Given the head of a singly linked list, return true if it is a
palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        while stack:
            curr = stack.pop()
            if curr != slow.val:
                return False
            slow = slow.next
        return True


# follow up:
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def recursive(left, right):
            if right.next:
                left, result = recursive(left, right.next)
                if result is False:
                    return left, False
                else:
                    left = left.next
            return left, left.val == right.val
        _, res = recursive(head, head)
        return res
