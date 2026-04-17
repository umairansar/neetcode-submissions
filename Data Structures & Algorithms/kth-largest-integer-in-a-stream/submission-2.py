class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap) 
        n = len(nums)
        while n - k > 0:
            heapq.heappop(self.heap)
            n -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        n = len(self.heap)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
