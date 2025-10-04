# 2269 Find the K-Beauty of a Number - Easy
# https://leetcode.com/problems/find-the-k-beauty-of-a-number
# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
# It has a length of k.
# It is a divisor of num.
# Given integers num and k, return the k-beauty of num.
# Tags: Math | String | Sliding Window

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        result = 0

        for i in range(len(s) - k + 1):
            sub = int(s[i:i+k])   
            if sub != 0 and num % sub == 0:
                result += 1
        return result