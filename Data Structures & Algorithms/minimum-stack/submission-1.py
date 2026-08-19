class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=float('inf')
        self.minStack=[]
        self.minStack.append(self.min)
        self.prev=0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<self.min:
            self.min=val
            self.prev=self.minStack.pop()
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack[-1]==self.minStack[0]:
            self.minStack.pop()
            self.minStack.append(self.prev)
        self.stack.pop()
            

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
