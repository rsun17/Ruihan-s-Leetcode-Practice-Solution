# 0409 Longest Palindrome - Easy
# https://leetcode.com/problems/longest-palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Tags: Hash Table | String | Greedy
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        oddCount = False
        
        for count in freq.values():
            length += count // 2 * 2

            if count % 2 == 1:
                oddCount = True
            
        if oddCount == True:
            length += 1

        return length