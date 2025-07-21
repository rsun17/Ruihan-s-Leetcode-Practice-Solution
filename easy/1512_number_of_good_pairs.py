# 1512 Number of Good Pairs - Easy
# https://leetcode.com/problems/number-of-good-pairs/
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# Tags: Array | Hash Table | Math | Counting
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict = {}
        count = 0

        for num in nums:
            if num in dict:
                count += dict[num]
                dict[num] += 1
            else:
                dict[num] = 1    
        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numIdenticalPairs([1,2,3,1,1,3]))
    print(sol.numIdenticalPairs([1,1,1,1]))
    print(sol.numIdenticalPairs([1,2,3]))