class MinStack:

    def __init__(self):
        self.stack  = []
        self.history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.history:
            self.history.append(val)
        else:
            self.history.append(min(val, self.history[-1]))

    def pop(self) -> None:
        self.history.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.history[-1]