# 2160 Minimum Sum of Four Digit Number After Splitting Digits - Easy
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
# You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
# Return the minimum possible sum of new1 and new2.
# Tags: Math | Greedy| Sorting

class Solution:
    def minimumSum(self, num: int) -> int:
        digit = []
        while num > 0:
            digit.append(num % 10)
            num //= 10
        digit.reverse()
        digit.sort(key=lambda x: x)

        num1 = 10 * digit[0] + digit[3]
        num2 = 10 * digit[1] + digit[2]
        return num1 + num2

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSum(4009))
    print(sol.minimumSum(2932))