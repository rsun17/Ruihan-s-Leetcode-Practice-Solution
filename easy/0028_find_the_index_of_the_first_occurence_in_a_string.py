# Find the Index of the First Occurrence in a String - Easy
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Tags: Two Pointers | String | String Matching

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))