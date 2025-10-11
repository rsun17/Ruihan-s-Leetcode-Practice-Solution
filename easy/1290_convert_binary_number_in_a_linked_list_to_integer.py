# 1290 Convert Binary Number in a Linked List to Integer - Easy
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# Tags: Linked List | Math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary = []
        while head:
            binary.append(head.val)
            head = head.next
        result = 0
        power = len(binary) - 1
        i = 0
        while power >= 0 and i < len(binary):
            result += (2 ** power) * int(binary[i])
            power -= 1
            i += 1
        return result