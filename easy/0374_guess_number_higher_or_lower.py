# 0374 Guess Number Higher or Lower - Easy
# https://leetcode.com/problems/guess-number-higher-or-lower
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.
# Tags: Binary Search | Interactive

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            if result == 0:
                return mid
            if result == -1:
                right = mid - 1
            if result == 1:
                left = mid + 1
        