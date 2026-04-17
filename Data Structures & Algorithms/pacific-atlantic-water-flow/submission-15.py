class Solution: #DFS, uphill, O(n·m) complexity with shared visited
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen = len(heights)
        colLen = len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        aVisited, pVisited = set(), set()

        def inBox(r, c):
            return (0 <= r < rowLen) and (0 <= c < colLen)

        def dfs_helper(r, c, visited):
            if r < 0 or c < 0 or r >= rowLen or c >= colLen:
                return
            
            if (r, c) in visited:
                return

            visited.add((r, c))
            for d in directions:
                newR = r + d[0]
                newC = c + d[1]
                if inBox(newR, newC) and heights[newR][newC] >= heights[r][c]:
                    dfs_helper(newR, newC, visited)

        for row in range(rowLen):
            dfs_helper(row, 0, pVisited)
            dfs_helper(row, colLen - 1, aVisited)
        for col in range(colLen):
            dfs_helper(0, col, pVisited)
            dfs_helper(rowLen - 1, col, aVisited)

        return list(aVisited & pVisited)