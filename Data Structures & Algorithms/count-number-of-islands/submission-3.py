class Solution: #template from hello interview
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        counter = 0
        visited = set()
        rowLen = len(grid)
        colLen = len(grid[0])

        def dfs(r, c):
            if (r, c) in visited:
                return

            if not (0 <= r < rowLen and 0 <= c < colLen):
                return

            if grid[r][c] == "0":
                return

            visited.add((r, c))     
            for d in directions:
                dfs(r + d[0], c + d[1])

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == "1" and (r, c) not in visited:
                    counter += 1
                    dfs(r, c)
        
        return counter
