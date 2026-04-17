class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            if node != parent[node]:
                return find(parent[node])
            return node

        def union(n1, n2, p1, p2):
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
        
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [1] * n
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            pu, pv = find(u-1), find(v-1)
            print(u-1, v-1, pu, pv)
            if pu == pv:
                return [u, v]
            else:
                union(u-1, v-1, pu, pv)
        return None
