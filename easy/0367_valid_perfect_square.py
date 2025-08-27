# 0367 Valid Perfect Square - Easy
# https://leetcode.com/problems/valid-perfect-square
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# Tags: Math | Binary Search

import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        root = math.isqrt(num)
        return root ** 2 == num

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPerfectSquare(144))