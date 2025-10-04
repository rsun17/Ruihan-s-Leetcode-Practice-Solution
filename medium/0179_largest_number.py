# 0179 Largest Number - Medium
# https://leetcode.com/problems/largest-number/
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Tags: Array | String | Greedy | Sorting

from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)  

        num = ""
        for i in range(len(nums)):
            num += nums[i]   
            
        return "0" if num[0] == "0" else num