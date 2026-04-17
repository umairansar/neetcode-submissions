class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(n, par):
            if n in visited:
                print("visited", visited, "n", n)
                return False

            visited.add(n)
            print("n", n, "visited", visited)

            if len(graph[n]) == 0:
                print("valid", n)
                return True

            result = True
            for i in graph[n]:
                if i != par:
                    res = dfs(i, n)
                    result &= res
            print(n, result)
            return result

        print(graph)
        r = dfs(0, -1)
        print(len(visited))
        return r and len(visited) == n
       