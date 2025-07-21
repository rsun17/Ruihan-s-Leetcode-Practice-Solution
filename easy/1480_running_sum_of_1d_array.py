# 1480 Running Sum of 1d Array - Easy
# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Tags: Array | Prefix Sum
from typing import List

class Solution:
    def runningSum(self, nums: List[int])->List[int]:
        result = []
        current_sum = 0
        for num in nums:
            current_sum += num
            result.append(current_sum)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.runningSum([1, 2, 3, 4]))
