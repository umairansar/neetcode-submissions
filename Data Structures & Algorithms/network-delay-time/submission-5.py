class Solution:
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
            # print(heap, distances)
            t, u = heapq.heappop(heap)
            if t > distances[u-1]:
                continue
            # distances[u-1] = t
            neighbours = edges.get(u, [])
            for ti, vi in neighbours:
                newT = t + ti
                if newT < distances[vi-1]:
                    distances[vi-1] = t + ti #wrong
                    heapq.heappush(heap, (newT, vi))
        
        # print(distances)
        if float('inf') in distances:
            return -1
        else:
            return max(distances)