# 1823 Find the Winner of the Circular Game - Medium
# https://leetcode.com/problems/find-the-winner-of-the-circular-game
# Given the number of friends, n, and an integer k, return the winner of the game.
# Tags: Array | Math | Recursion | Queue | Simulation
from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = deque(range(1, n + 1))

        while len(circle) > 1:
            steps = (k - 1) % k
            circle.rotate(-steps)
            circle.popleft()
        return circle[0]