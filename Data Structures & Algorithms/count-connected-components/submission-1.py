class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(i):
            if i in visited:
                return

            visited.add(i)
            for j in graph[i]:
                dfs(j)

        visited = set()
        counter = 0
        for i in range(n):
            if i not in visited:
                counter += 1 # Enter first time so increment
                dfs(i)

        return counter