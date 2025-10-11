# 0003 Longest Substring Without Repeating Characters - Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters
# Given a string s, find the length of the longest substring without duplicate characters.
# Tags: Hash Table | String | Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            count = max(count, right - left + 1)
            
        return count