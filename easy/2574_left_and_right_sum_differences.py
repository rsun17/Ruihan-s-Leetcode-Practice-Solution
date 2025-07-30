# 2574 Left and Right Sum Differences - Easy
# https://leetcode.com/problems/left-and-right-sum-differences/
# You are given a 0-indexed integer array nums of size n. Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.
# Tags: Array | Prefix Sum

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = self.leftSum(nums)
        right = self.rightSum(nums)
        return [abs(left[i] - right[i]) for i in range(len(nums))]
    
    def leftSum(self, nums: List[int]) -> List[int]:
        leftSum = []
        for i in range(len(nums)):
            leftSum.append(sum(nums[:i]))
        return leftSum
    
    def rightSum(self, nums: List[int]) -> List[int]:
        rightSum = []
        for i in range(len(nums)):
            rightSum.append(sum(nums[i+1:len(nums)]))
        return rightSum
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.leftRightDifference([10,4,8,3]))


