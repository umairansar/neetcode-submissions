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
            u = queue.popleft() #pop also works. Why? ⬇️
            res.append(u)

            for v in prereqs[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)
        
        return res if len(res) == numCourses else [] #detects cycles
        '''
        Because topological sort doesn't require FIFO ordering — 
        any order works as long as you only process nodes with indegree == 0.
        
        The only guarantee Kahn's needs:
        A node enters the queue/stack ONLY when indegree == 0
        meaning ALL its prerequisites are already processed
        Whether you pick from front or back doesn't affect correctness — every node in the queue is already "safe" to process.
        '''