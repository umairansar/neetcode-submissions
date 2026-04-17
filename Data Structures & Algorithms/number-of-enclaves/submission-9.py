class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            for c, d in dirs:
                dfs(i + c, j + d)

        print("rows", rows, "cols", cols)
        for row in range(rows):
            print(row)
            if grid[row][0]: dfs(row, 0)
            if grid[row][cols-1]: dfs(row, cols-1)
        for col in range(cols):
            if grid[0][col]: dfs(0, col)
            if grid[rows-1][col]: dfs(rows-1, col)

        return sum([grid[r][c] for r in range(rows) for c in range(cols)])