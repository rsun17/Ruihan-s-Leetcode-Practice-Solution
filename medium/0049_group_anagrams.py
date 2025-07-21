# 0049 Group Anagram - Medium
# https://leetcode.com/problems/group-anagrams/
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Tags: Array | Hash Table | String | Sorting
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in dict:
                dict[key] = []
            dict[key].append(word)
        return list(dict.values())
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))