class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Need to add both cuz no way to know how to start from root
        If i try finding starting root, it means same thing as solving
        the problem, cuz non-tree graphs have no root.
        '''
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) # Need to add both directions

        visited = set()
        def dfs(n, par):
            if n in visited:
                return False

            visited.add(n)

            if len(graph[n]) == 0:
                return True

            result = True
            for i in graph[n]:
                if i != par: # Don't revisit the parent
                    res = dfs(i, n)
                    result &= res
            return result

        r = dfs(0, -1)
        return r and len(visited) == n
       