# 0169 Majority Element - Easy
# https://leetcode.com/problems/majority-element
# Given an array nums of size n, return the majority element.
# Tags: Array | Hash Table | Divide and Conquer | Sorting | Counting

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x)
        return nums[len(nums)//2]