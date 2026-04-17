class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        priority = [(-math.sqrt(x**2 + y**2), [x, y]) for x, y in points]
        heapq.heapify(priority)
        while len(priority) > k:
            heapq.heappop(priority)
        return [point[1] for point in priority]