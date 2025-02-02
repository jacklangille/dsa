class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack:
            val = min(val, self.minStack[-1])
        else:
            val = min(val, val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop() 
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



min_stack = MinStack()

min_stack.push(5)
min_stack.push(7)
min_stack.push(-1)
print(min_stack.getMin())
min_stack.push(-6)
print(min_stack.getMin())
min_stack.pop()
print(min_stack.getMin())
