# 0083 Remove Duplicates from Sorted List - Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-list
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        temp = head
        while temp:
            if temp.next and temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head