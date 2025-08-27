# 0350 - Intersection of Two Arrays II - Easy
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Tags: Array | Hash Table | Two Pointers | Binary Search | Sorting

from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        intersection = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j+=1

        return intersection

if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect([1,2,2,1], [2,2]))