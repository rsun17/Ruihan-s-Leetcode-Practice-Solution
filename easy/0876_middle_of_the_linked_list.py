# 0876 Middle of the Linked List - Easy
# https://leetcode.com/problems/middle-of-the-linked-list
# Given the head of a singly linked list, return the middle node of the linked list.
# Tags: Linked List | Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow