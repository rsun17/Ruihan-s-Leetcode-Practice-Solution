# 0804 Unique Morse Code Words - Easy
# https://leetcode.com/problems/unique-morse-code-words/
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# Return the number of different transformations among all words we have.
# Tags: Array | Hash Table | String
from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]

        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        morse_dict = dict(zip(alphabet, morse_code))
        morse_translation = []

        for word in words:
            translation = ""
            for i in word:
                translation += morse_dict[i]
            morse_translation.append(translation)
        
        return len(set(morse_translation))


print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

