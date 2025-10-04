# 1700 Number of Students Unable to Eat Lunch - Easy
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch
# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
# Tags: Array | Stack | Queue | Simulation

from typing import List
from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = deque(sandwiches)
        rotations = 0

        while queue and stack:
            if queue[0] == stack[0]:
                    queue.popleft()
                    stack.popleft()
                    rotations = 0
            else:
                queue.append(queue.popleft())
                rotations += 1
                if rotations == len(queue):
                     break
        return len(queue)