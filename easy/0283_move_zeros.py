# 0283 Move Zeros - Easy
# https://leetcode.com/problems/move-zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Tags: Array | Two Pointers

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
                
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
        