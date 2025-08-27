# 0026 Remove Duplicates from Sorted Array - Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Tags: Array | Two Pointers

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,2]))