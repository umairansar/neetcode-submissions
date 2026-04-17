class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj: Dict[int, Set[int]] = dict()

        for course, prerequisite in prerequisites:
            if course == prerequisite:
                return False
            if prerequisite in adj:
                adj[prerequisite].add(course)
            else:
                adj[prerequisite] = {course}

        print(adj)
        
        visited = [False] * numCourses
        entry = [-1] * numCourses
        exit = [-1] * numCourses
        def dfs(course:int, step:int):
            #already entered before and not yet exited
            if entry[course] > 1 and entry[course] < step and exit[course] == -1:
                return True, step
            
            hasCycle = False
            visited[course] = True
            entry[course] = step
            neighbours = adj[course] if course in adj else []
            for neighbour in neighbours:
                step+=1
                hasCycle, step = dfs(neighbour, step)
                if hasCycle:
                    break

            step+=1
            exit[course] = step
            return hasCycle, step
        
        hasCycle, _ = dfs(0, 1)

        if hasCycle:
            return False
        return True 

        