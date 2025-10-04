# Merge Sorted Array - Easy
# https://leetcode.com/problems/merge-sorted-array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# Tags: Array | Two Pointers | Sorting

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1          
        j = n - 1          
        k = m + n - 1      

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

       
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

if __name__ == "main":
    sol = Solution()
    print(sol.merge())