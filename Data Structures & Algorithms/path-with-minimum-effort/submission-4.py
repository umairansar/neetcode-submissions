class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        efforts = {(0, 0):0}
        heap = [(0, (0, 0))]

        while heap:
            effort, (i, j) = heapq.heappop(heap)

            neighbours = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
            for x, y in neighbours:
                if not (0 <= x < n and 0 <= y < m):
                    continue
                newEffort = max(effort,  abs(heights[x][y] - heights[i][j]))
                if (x,y) not in efforts:
                    efforts[(x, y)] = newEffort
                    heapq.heappush(heap, (newEffort, (x, y)))
                elif newEffort < efforts[(x, y)]:
                    efforts[(x, y)] = newEffort
                    heapq.heappush(heap, (newEffort, (x, y)))
        return efforts[(n-1, m-1)]

