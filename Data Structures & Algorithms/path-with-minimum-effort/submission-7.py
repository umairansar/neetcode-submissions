class Solution:
    '''
    Djikstra -> O((V + E) log V) time, O(V) space
    
    /Early termination (Added as an afterthought)
    When any node is popped from the min-heap, its cost is optimal. 
    This is the core invariant: Pop = optimal

    /Pruning
    When newEffort >= efforts[(x,y)] you skip the heap push, which means:
    Any path through (x,y) with higher effort is silently discarded and never explored
    '''
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        efforts = {(0, 0):0}
        heap = [(0, (0, 0))]

        while heap:
            effort, (i, j) = heapq.heappop(heap)
            if (i, j) == (n-1, m-1): # Early termination optimization
                return effort   # always works for djikstra

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

