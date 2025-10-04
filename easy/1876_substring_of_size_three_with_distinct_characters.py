# 1876 Substring of Size Three with Distinct Characters - Easy
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Tags: Hash Table | String | Sliding Window | Counting

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        count = 0
        for i in range(len(s) - 2):
            if len(set(s[i: i + 3])) == 3:
                count += 1
        return count 