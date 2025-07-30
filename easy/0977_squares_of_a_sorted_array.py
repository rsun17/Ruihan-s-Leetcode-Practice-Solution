# 0977 Squares of a Sorted Array - Easy
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Tags: Array | Two Pointers | Sorting

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i] = nums[i] * nums[i]
        # nums.sort(key=lambda x: x)
        # return nums
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedSquares([-7,-3,2,3,11]))