import math


class MinStack:
    minS = [math.inf]

    def __init__(self):
        self.stck = []

    def push(self, val: int) -> None:
        self.stck.append(val)
        if val <= self.minS[-1]:
            self.minS.append(val)

    def pop(self) -> None:
        p = self.stck.pop()
        if p == self.minS[-1]:
            self.minS.pop()

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return self.minS[-1]


obj = MinStack()
obj.push(-1)
print(obj.top())
print(obj.getMin())

