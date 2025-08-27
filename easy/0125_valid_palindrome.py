# 0125 Valid Palindrome - Easy
# https://leetcode.com/problems/valid-palindrome
# Given a string s, return true if it is a palindrome, or false otherwise.
# Tags: Two Pointers | String

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True