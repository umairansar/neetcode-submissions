class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Construct a graph, adjacency List
        Check for cycles
        '''
        def dfs(n, path):
            if n in path:
                return True # Return true for cycle 

            if n in visited:
                return False # Some other dfs would've returned true for cycles

            visited.add(n)

            result = False
            for prereq in graph[n]:
                res = dfs(prereq, path | {n})
                result |= res
            return result

        graph = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = set() # visited shared
        for node in range(numCourses):
            if dfs(node, set()): # path unique
                return False # Has Cycles
        return True

        # Decide when to keep visited shared Vs when to pass in dfs
        # Here, needed to avoid dfs if already visited in prior dfs,
        # Hence, visted was shared.
