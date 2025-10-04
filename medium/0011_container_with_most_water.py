# 0011 Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Tags: Array | Two Pointers | Greedy

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            best = max(best, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best