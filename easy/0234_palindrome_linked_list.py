# 0234 Palindrome Linked List - Easy
# https://leetcode.com/problems/palindrome-linked-list
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Tags: Linked List | Two Pointers | Stack | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val = []
        while head:
            val.append(head.val)
            head = head.next
        left, right = 0, len(val) - 1

        while left < right:
            if val[left] != val[right]:
                return False
            left += 1
            right -= 1
        return True