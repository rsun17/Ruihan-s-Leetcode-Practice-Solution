# 1047 Remove All Adjacent Duplicates In String - Easy
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
# Tags: String | Stack 

from collections import deque

class Solution:

    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates('abbaca'))