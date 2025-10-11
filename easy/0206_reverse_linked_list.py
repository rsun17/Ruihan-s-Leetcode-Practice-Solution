# 0206 Reverse Linked List - Easy
# https://leetcode.com/problems/reverse-linked-list
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Tags: Linked List | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev