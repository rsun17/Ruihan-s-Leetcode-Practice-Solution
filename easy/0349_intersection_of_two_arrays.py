# 0349 Intersection of Two Arrays - Easy
# https://leetcode.com/problems/intersection-of-two-arrays/
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
# Tags: Array | Hash Table | Two Pointers | Binary Search

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))