# 1122 Relative Sort Array - Easy
# https://leetcode.com/problems/relative-sort-array
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
# Tags: Array | Hash Table | Sorting | Counting Sort

from typing import List
class Solution:
    def relativeSortArray(self, arr1, arr2):
        result = []

        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    result.append(arr1[j])
                    arr1[j] = -1
        arr1.sort(key=lambda x: x)
        
        for num in arr1:
            if num != -1:
                result.append(num)
                
        return result