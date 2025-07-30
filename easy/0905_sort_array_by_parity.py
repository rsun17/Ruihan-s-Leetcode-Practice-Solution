# 0905 Sort Array By Parity - Easy
# https://leetcode.com/problems/sort-array-by-parity/
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Tags: Array | Two Pointers | Sorting

from typing import List
class Solution:
     def sortArrayByParity(self, nums: List[int]) -> List[int]:
          left = 0

          for i in range(len(nums)):
               if nums[i] % 2 == 0:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
          return nums
    #       even = []
    #       odd = []
    #       for i in range(len(nums)):
    #            if self.isEven(nums[i]):
    #                 even.append(nums[i])
    #            else:
    #                 odd.append(nums[i])
               
    #       return even + odd

    #  def isEven(self, num: int) -> bool:
    #       return num % 2 == 0
if __name__ == "__main__":
     sol = Solution()
     print(sol.sortArrayByParity([3, 1, 2, 4]))