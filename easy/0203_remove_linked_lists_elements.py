# 0203 Remove Linked Lists Elements - Easy
# https://leetcode.com/problems/remove-linked-list-elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
# Tags: Linked List | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
       result = ListNode(0, head)
       current = result
  
       while current:
           while current.next and current.next.val == val:
               current.next = current.next.next
           current = current.next


       return result.next
