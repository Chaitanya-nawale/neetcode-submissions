class MinStack:

    def __init__(self):
        self.internal_stack = []

    def push(self, val: int) -> None:
        if len(self.internal_stack) != 0: 
            self.internal_stack.append([val, min(self.internal_stack[-1][1], val)])
        else:
            self.internal_stack.append([val, val])
        return None

    def pop(self) -> None:
        if len(self.internal_stack) != 0:
            self.internal_stack.pop()
        return None

    def top(self) -> int:
        return self.internal_stack[-1][0]

    def getMin(self) -> int:
        return self.internal_stack[-1][1]
        
