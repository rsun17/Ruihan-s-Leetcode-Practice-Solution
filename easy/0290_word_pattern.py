# 0290 Word Pattern - Easy
# https://leetcode.com/problems/word-pattern/
# Given a pattern and a string s, find if s follows the same pattern.
# Tags: Hash Table | String

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        p2w = {}
        w2p = {}

        for ch, w in zip(pattern, words):
            if ch in p2w and p2w[ch] != w:
                return False
            if w in w2p and w2p[w] != ch:
                return False
            p2w[ch] = w
            w2p[w] = ch

        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))