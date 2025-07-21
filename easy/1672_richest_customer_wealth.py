# 1672 Richest Customer Wealth - Easy
# https://leetcode.com/problems/richest-customer-wealth/
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# Tags: Array | Matrix

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0

        for i in range(len(accounts)):
            if self.sumWealth(accounts[i]) > maxSum:
                maxSum = self.sumWealth(accounts[i])
        return maxSum



    def sumWealth(self, account: List[int]) -> int:
        sum = 0
        for num in account:
            sum += num
        return sum
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumWealth([[1,5],[7,3],[3,5]]))