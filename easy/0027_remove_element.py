# 0027 Remove Element - Easy
# https://leetcode.com/problems/remove-element/
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Tags: Array | Two Pointers

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement([0,1,2,2,3,0,4,2], 2))