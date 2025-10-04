# 0232 Implement Queue Using Stacks - Easy
# https://leetcode.com/problems/implement-queue-using-stacks
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Tags: Stack | Design | Queue

class MyQueue:

    def __init__(self):
        self._in = []
        self._out = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        self.move()
        return self._out.pop()

    def peek(self) -> int:
        self.move()
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out

    def move(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()