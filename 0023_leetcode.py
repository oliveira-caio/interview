"""23. Merge k Sorted Lists

link: https://leetcode.com/problems/merge-k-sorted-lists/

problem: You are given an array of k linked-lists lists, each linked-list is
sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""


from heapq import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        heap = []
        
        for l in lists:
            while l:
                heappush(heap, l.val)
                l = l.next

        head = prev = None
        while heap:
            val = heappop(heap)
            node = ListNode(val)
            if not head:
                head = prev = node
            else:
                prev.next = node
                prev = prev.next

        return head


class Solution:
    def mergeKLists(self, lists):
        heap = []; head = temp = None

        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i, l.next))

        while heap:
            val, i, next_n = heappop(heap)
            node = ListNode(val)
            if next_n:
                heappush(heap, (next_n.val, i, next_n.next))
            if not head:
                head = temp = node
            else:
                temp.next = node
                temp = temp.next

        return head
