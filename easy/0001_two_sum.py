# 0001 Two Sum - Easy
# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Tags: Array | Hash Table

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int)->List[int]:
        # modifiedList = [target - x for x in nums]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(modifiedList)):
        #         if nums[i] == modifiedList[j]:
        #             return [i,j]
        num_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1, 2, 3, 4], 5))