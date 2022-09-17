from collections import deque

class MinStack:

    def __init__(self):
        self.s = deque()
        self.min_stack = deque()
        
    def push(self, val: int) -> None:
        self.s.append(val)
        
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        if len(self.s) > 0:
            val = self.s.pop()
            if len(self.min_stack) > 0 and self.min_stack[-1] == val:
                self.min_stack.pop()
            return val

    def top(self) -> int:
        return self.s[-1] if len(self.s) > 0 else None

    def getMin(self) -> int:
        return self.min_stack[-1] if len(self.min_stack) > 0 else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()