# 0209 Minimum Size Subarray Sum - Medium
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Tags: Array | Binary Search | Sliding Window | Prefix Sum

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        result = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                result = min(result, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return 0 if result == float('inf') else result