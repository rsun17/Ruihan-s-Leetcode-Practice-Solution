# 0134 Gas Station - Medium
# https://leetcode.com/problems/gas-station/
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
# Tags: Array | Greedy
from typing import List

class Solution:
   def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
       total = 0
       current = 0
       start = 0


       for i in range(len(gas)):
           gain = gas[i] - cost[i]
           total += gain
           current += gain
           if current < 0:
               start = i + 1
               current = 0


       return -1 if total < 0 else start
