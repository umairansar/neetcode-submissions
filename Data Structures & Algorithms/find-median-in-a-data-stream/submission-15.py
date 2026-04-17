class MedianFinder:

    def __init__(self):
        self.timeline = []
        self.left = [] #max heap
        self.right = [] #min heap

    def addNum(self, num: int) -> None:
        def rebalance():
            diff = len(self.left) - len(self.right)
            if diff > 0: #Rebalance left by moving to right
                while len(self.left) - len(self.right) > 1:
                    val = -heapq.heappop(self.left)
                    heapq.heappush(self.right, val)
            else: #Rebalance right by moving to left
                while len(self.right) - len(self.left) > 1:
                    val = heapq.heappop(self.right)
                    heapq.heappush(self.left, -val)

        self.timeline.append(num)
        n = len(self.timeline) 
        if n in (1, 2):
            heapq.heappush(self.left, -num)
        else:
            if num < -self.left[0] and num < self.right[0]:
                heapq.heappush(self.left, -num)
            elif num > -self.left[0] and num > self.right[0]:
                heapq.heappush(self.right, num)
            elif num >= -self.left[0] and num <= self.right[0]:
                heapq.heappush(self.left, -num)  
        rebalance()

    def findMedian(self) -> float:
        nl = len(self.left)
        nr = len(self.right) 
        if nl > nr:
            return -self.left[0]
        elif nr > nl:
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
        