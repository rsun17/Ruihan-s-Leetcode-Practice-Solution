# 0141 Linked List Cycle - Easy
# https://leetcode.com/problems/linked-list-cycle/
# Return true if there is a cycle in the linked list. Otherwise, return false.
# Tags: Hash Table | Linked List | Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False