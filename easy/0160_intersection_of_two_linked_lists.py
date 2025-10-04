# 0160 Intersection of Two Linked Lists - Easy
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# Tags: Hash Table | Linked List | Two Pointers

from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:   
            return None

        p, q = headA, headB
        while p is not q:          
            p = p.next if p else headB
            q = q.next if q else headA

        return p