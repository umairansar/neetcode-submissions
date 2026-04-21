class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        row1s = [sum(grid[i]) for i in range(r)]
        col1s = [sum([grid[j][i] for j in range(r)]) for i in range(c)]
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (row1s[i] > 1 or col1s[j] > 1):
                    res += 1
        return res
