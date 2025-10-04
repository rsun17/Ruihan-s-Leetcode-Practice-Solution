# 2696 Minimum String Length After Removing Substring - Easy
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings
# You are given a string s consisting only of uppercase English letters.
# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.
# Return the minimum possible length of the resulting string that you can obtain.
# Tags: String | Stack | Simulation

class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for ch in s:
            if stack and ((stack[-1] == 'A' and ch == 'B') or stack[-1] == 'C' and ch == 'D'):
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)