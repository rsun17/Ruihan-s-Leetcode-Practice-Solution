# 0268 Missing Number - Easy
# https://leetcode.com/problems/missing-number/
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Tags: Array | Hash Table | Math | Binary Search | Bit Manipulation | Sorting

from typing import List

class Solution: 
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)