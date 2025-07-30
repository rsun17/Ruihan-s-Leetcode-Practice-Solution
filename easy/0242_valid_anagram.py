# 0242 Valid Anagram - Easy
# https://leetcode.com/problems/valid-anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Tags: Hash Table | String | Sorting

from collections import defaultdict
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for word in s:
            count[word] += 1
        
        for word in t:
            count[word] -= 1
        
        for value in count.values():
            if value != 0:
                return False
        return True
        