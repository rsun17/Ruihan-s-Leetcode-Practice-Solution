# 0027 Next Permutation - Medium
# https://leetcode.com/problems/next-permutation/
# Given an array of integers nums, find the next permutation of nums.The replacement must be in place and use only constant extra memory.
# Tags: Array | Two pointers

from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if self.isDecreasing(nums):
            nums.reverse()
            return
        
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        j = len(nums) - 1
        while j > 0 and nums[j] <= nums[i-1]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = reversed(nums[i:])
    
    def isDecreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkSequence([3, 1, 2, 1]))