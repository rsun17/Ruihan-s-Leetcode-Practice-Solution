# 658 Find K Closest Elements - Medium
# https://leetcode.com/problems/find-k-closest-elements/
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# Tags: Array | Two Pointers | Binary Search | Sliding Window | Sorting | Heap
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0 , len(arr) - k

        while low < high:
            mid = (high + low)//2

            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid
        return arr[low:low + k]
