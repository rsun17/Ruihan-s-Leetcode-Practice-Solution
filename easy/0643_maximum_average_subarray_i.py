# 0643 Maximum Average Subarray I - Easy
# https://leetcode.com/problems/maximum-average-subarray-i
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Tags: Array | Sliding Window

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[:k])
        maxSum = currentSum
        
        for i in range(k, len(nums)):
            currentSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, currentSum)
        return maxSum / k