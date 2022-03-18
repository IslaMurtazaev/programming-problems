# Min Stack https://leetcode.com/problems/min-stack/

class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack or self.min_stack[-1][0] > val:
            self.min_stack.append([val, 1])
        elif self.min_stack[-1][0] == val:
            self.min_stack[-1][1] += 1
        self.stack.append(val)

    def pop(self) -> None:
        if self.min_stack[-1][0] == self.stack[-1]:
            if self.min_stack[-1][1] == 1:
                self.min_stack.pop()
            else:
                self.min_stack[-1][1] -= 1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
