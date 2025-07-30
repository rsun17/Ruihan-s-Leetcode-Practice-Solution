# 0217 Contains Duplicate - Easy
# https://leetcode.com/problems/contains-duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Tags: Array | Hash Table | Sorting

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
          return len(nums) != len(set(nums))