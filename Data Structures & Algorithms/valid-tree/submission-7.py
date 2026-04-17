class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(n, par):
            if n in visited:
                return False

            visited.add(n)

            if len(graph[n]) == 0:
                return True

            result = True
            for i in graph[n]:
                if i != par:
                    res = dfs(i, n)
                    result &= res
            return result

        r = dfs(0, -1)
        return r and len(visited) == n
       