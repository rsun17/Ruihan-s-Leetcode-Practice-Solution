# 0225 Implement Stack Using Queues - Easy
# https://leetcode.com/problems/implement-stack-using-queues
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# Tags: Stack | Design | Queue
from collections import deque

class MyStack:

    def __init__(self):
        self.in_queue = deque()
        self.out_queue = deque()

    def push(self, x: int) -> None:
        self.in_queue.append(x)

    def pop(self) -> int:
        self.move()
        top = self.in_queue.popleft()
        self.in_queue, self.out_queue = self.out_queue, self.in_queue
        return top

    def top(self) -> int:
        self.move()
        top = self.in_queue.popleft()
        self.out_queue.append(top)
        self.in_queue, self.out_queue = self.out_queue, self.in_queue
        return top

    def empty(self) -> bool:
        return not self.in_queue and not self.out_queue

    def move(self):
        while len(self.in_queue) > 1:
            self.out_queue.append(self.in_queue.popleft())




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()