class MinStack:

    def __init__(self):
        self.top_pointer = -1
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_pointer+=1

    def pop(self) -> None:
        if self.top_pointer != -1:
            self.stack.pop(self.top_pointer)
            self.top_pointer-=1

    def top(self) -> int:
        if self.top_pointer != -1:
            return self.stack[self.top_pointer]

    def getMin(self) -> int:
        if self.top_pointer != -1:
            return min(self.stack)
        
