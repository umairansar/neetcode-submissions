from collections import deque

class Solution: #Kahn's algorithm
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = { i:[] for i in range(numCourses) }
        prereqs = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            courses[crs].append(pre)
            prereqs[pre].append(crs)

        indegrees = { c: len(p) for c, p in courses.items() }
        queue = deque({ c for c, p in courses.items() if p == [] })
        res = []
        while queue:
            print(queue)
            u = queue.popleft()
            res.append(u)

            for v in prereqs[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)
        
        print(res)
        return res if len(res) == numCourses else []