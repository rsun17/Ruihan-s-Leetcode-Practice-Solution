# 0933 Number of Recent Calls - Easy
# https://leetcode.com/problems/number-of-recent-calls/
# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
# Implement the RecentCounter class:
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# Tags: Design | Queue | Data Stream

from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        bound = t - 3000
        while self.queue and self.queue[0] < bound:
            self.queue.popleft()
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)