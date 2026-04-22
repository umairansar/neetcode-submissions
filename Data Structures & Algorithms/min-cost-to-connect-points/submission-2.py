class Solution:
    '''
    Kruskal's MST - basically sort by edges, then union find
    Without rank → tree can become skewed → find() becomes O(n)
    With rank + path compression → nearly O(1) amortized
    '''
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                diff = abs(x1 - x2) + abs(y1 - y2)
                edges.append((diff, i, j))

        edges.sort(key=lambda x: x[0])

        parents = [i for i in range(n)]
        ranks = [1 for i in range(n)]
        
        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if ranks[p1] > ranks[p2]: #why bother? 
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                parents[p1] = p2
                ranks[p2] += ranks[p1]
            return True

        res = 0
        for diff, u, v in edges:
            if union(u, v):
                res += diff

        return res