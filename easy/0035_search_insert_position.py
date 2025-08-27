# 0035 Search Insert Positiuon - Easy
# https://leetcode.com/problems/search-insert-position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# Tags: Array | Binary Search
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: 
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        
        if nums[right] < target:
            return right + 1
        elif nums[left] > target:
            return left
        else:
            return right