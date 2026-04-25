class Solution: # O() TLE fixes
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        starting node has time 0 all else infinity
        run djikstra using min heap on current node
        pop min node and insert child nodes - can use dict[times]
        '''
        distances = [0 if i == k else float('inf') for i in range(1, n+1)]
        edges = {}
        for u, v, t in times:
            edges[u] = edges.get(u, []) + [(t, v)]

        heap = [(0, k)]

        while heap:
            t, u = heapq.heappop(heap)
            if t > distances[u-1]:
                continue
            neighbours = edges.get(u, [])
            for ti, vi in neighbours:
                newT = t + ti
                if newT < distances[vi-1]:
                    distances[vi-1] = newT # I thought this wrong but this killed performance -> TLE
                    heapq.heappush(heap, (newT, vi))
        
        if float('inf') in distances:
            return -1
        else:
            return max(distances)