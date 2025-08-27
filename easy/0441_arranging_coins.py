# 0441 Arranging Coins - Easy
# https://leetcode.com/problems/arranging-coins
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
# Tags: Math | Binary Search
import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
    #    floor = 1
    #    count = 0
    #    while n >= floor:
    #        n = n - floor
    #        floor += 1
    #        count += 1
        
    #    return count
        return int((math.sqrt(8 * n + 1) - 1) // 2)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.arrangeCoins(6))
    