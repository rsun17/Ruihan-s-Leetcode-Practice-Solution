# 0387 First Unique Character in a String - Easy
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Tags: Hash Table | String | Queue | Counting

from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = deque()
        freq = {}
        for i, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            if freq[ch] == 1:
                queue.append(i)
            
            while queue and freq[s[queue[0]]] > 1:
                queue.popleft()

        return queue[0] if queue else -1