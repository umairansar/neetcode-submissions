class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Construct a graph, adjacency List
        Check for cycles
        '''
        visited = set()
        def dfs(n, path):
            if n in path:
                return True
                
            if n in visited:
                return False #Some other dfs would have returned true for cycles

            visited.add(n)

            result = False
            for prereq in graph[n]:
                res = dfs(prereq, path | {n})
                result |= res
            print("recursive, ", result)
            return result

        graph = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        print(graph)
        for node in range(numCourses):
            print("dfs (", node, ")")
            if dfs(node, set()):
                return False # Has Cycles
        return True
