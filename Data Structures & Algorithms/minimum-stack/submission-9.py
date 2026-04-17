class MinStack:

    def __init__(self):
        self.s = [] #(val, min)
        self.min = 100000000000

    def push(self, val: int) -> None:
        if val < self.min:
            self.s.append((val, val))
            self.min = val
        else:
            self.s.append((val, self.min))
        print(self.s)

    def pop(self) -> None:
        _, _ = self.s.pop()
        self.min = self.s[-1][1] if self.s else 100000000000

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.min
        
