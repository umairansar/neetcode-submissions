class Solution: #O(V+E) time and space
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i:[] for i in range(numCourses)}
        prereqs = {i:[] for i in range(numCourses)}
        for b, a in prerequisites:
            courses[b].append(a)
            prereqs[a].append(b)

        def dfs(i, path):
            if i in path: #cycle is detected by path n dfs not global visited
                return False
            if i in visited:  # already proven no cycle from here
                return True

            visited.add(i)

            res = True
            for j in prereqs[i]:
                res &= dfs(j, path | {i})
            return res

        visited = set()
        for c in range(numCourses):
            if c not in visited and not dfs(c, set()):
                return []
        
        res = []
        visited = set()
        starters = [c for c, p in courses.items() if p == []]
        indegrees = {c: len(p) for c, p in courses.items()}
        for starter in starters:
            queue = [starter]
            while queue:
                u = queue.pop()
                if u not in visited:
                    res.append(u)
                    visited.add(u)
                    vs = prereqs[u]
                    for v in vs:
                        if indegrees[v] == 1:
                            queue.append(v)
                        else:
                            indegrees[v] -= 1

        return res