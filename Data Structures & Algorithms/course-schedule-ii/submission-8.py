class Solution:
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
        starters = [c for c, p in courses.items() if p == []]
        for starter in starters:
            queue = [starter]
            while queue:
                u = queue.pop()
                res.append(u)
                vs = prereqs[u]
                for v in vs:
                    queue.append(v)

        return res



        

            