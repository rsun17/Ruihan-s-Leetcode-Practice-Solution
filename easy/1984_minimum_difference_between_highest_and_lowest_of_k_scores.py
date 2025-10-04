# 1984 Minimum Difference Between Highest and Lowest of K Scores - Easy
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores
# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.
# Tags: Array | Sliding Window | Sorting
from typing import List 

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: x)
        if k <= 1:
            return 0
        diff = float('inf')
        for i in range(len(nums) - k + 1):
            diff = min(diff, nums[i + k - 1] - nums[i])
        return diff