# 0561 Array Partition - Easy
# https://leetcode.com/problems/array-partition/
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
# Tags: Array | Greedy | Sorting | Counting Sort

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x)
        i = 0
        sum = 0

        while i < len(nums):
            sum += min(nums[i], nums[i+1])
            i += 2

        return sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.arrayPairSum([6,2,6,5,1,2]))