class StockSpanner: #mono decreasing

    def __init__(self):
        self.prices = []
        self.stack = []
        self.n = 0

    def next(self, price: int) -> int:
        self.prices.append(price)
        self.n += 1
        while self.stack and price > self.stack[-1][0]:
            self.stack.pop()
        self.stack.append((price, self.n-1))
        prev = -1
        for i in range(len(self.stack) - 2, -1, -1):
            if self.stack[i][0] > self.stack[-1][0]:
                prev = self.stack[i][1]
                break
        return self.stack[-1][1] - prev


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)