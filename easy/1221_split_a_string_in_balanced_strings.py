# 1221 Split a String in Balanced Strings - Easy
# https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.
# Tags: String | Greedy | Counting 

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        maxNum = 0

        for i in range(len(s)):
            if s[i] == "R":
                count += 1
            elif s[i] == "L":
                count -= 1
            
            if count == 0:
                maxNum += 1
            
        return maxNum