class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen = len(heights)
        colLen = len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        atlantic = set()
        pacific = set()

        def inBox(r, c):
            return (0 <= r < rowLen) and (0 <= c < colLen)

        def dfs_helper(r, c, path, visited):
            if r >= rowLen or c >= colLen:
                atlantic.update(path)
                return

            if r < 0 or c < 0:
                pacific.update(path)
                return
            
            if (r, c) in visited:
                return

            visited.add((r, c))
            for d in directions:
                newR = r + d[0]
                newC = c + d[1]
                if (inBox(newR, newC) and heights[newR][newC] <= heights[r][c]) or not inBox(newR, newC):
                    dfs_helper(newR, newC, path + [(r, c)], visited)
            return

        for row in range(rowLen):
            for col in range(colLen):
                dfs_helper(row, col, [], set())
                
        print(pacific, atlantic)
        return list(pacific & atlantic)