class MedianFinder: # O(shit)
    # 1 => 1
    # 1, 2 => 
    # 1, 2, 3
    # 1, 2, 3, 4

    def __init__(self):
        self.heap = []

    # O(log n)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num);
        print("Push", num)

    # O(nlogn)
    def findMedian(self) -> float:
        print("Median")
        copy = self.heap[:]
        if len(self.heap) % 2 == 1:
            index = len(self.heap) // 2
            val = 0
            while index >= 0:
                val = heapq.heappop(copy)
                index -= 1
            return val
        
        index = len(self.heap) // 2
        val = 0
        while index > 0:
            val = heapq.heappop(copy)
            index -= 1

        return (val + heapq.heappop(copy)) / 2 