class Solution:
    '''
    
    '''
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [0 if i == src else float('inf') for i in range(n)]
        jumps = [float('inf') for i in range(n)]
        edges = {}
        for s, d, dist in flights:
            edges[s] = edges.get(s, []) + [(d, dist)]
        # print("e", edges)
        heap = [(-1, 0, src)]
        while heap:
            # print("h", heap)
            k_, dist, u = heapq.heappop(heap)
            # print(k_, dist, u)
            # if dist > distances[u]: # had to remove it because even if distance > might need to update if k is lesser and leads to solution
            #     continue
            if k_ > jumps[u]: #can do this instead
                continue
            neighbours = edges.get(u, [])
            # print("ne", neighbours, jumps, distances)
            for v, dist2 in neighbours:
                newDist = dist + dist2
                newK = k_ + 1
                # print(newK, jumps[v], newDist, distances[v])
                if newK <= k and newDist <= distances[v]:
                    distances[v] = newDist
                    jumps[v] = newK
                    heapq.heappush(heap, (newK, newDist, v))
        return -1 if distances[dst] == float('inf') else distances[dst]