class Solution:
    '''
    Simple grid traversal O(m*n) time O(m+n) space
    converge sum of rows and sum of cols into individual lists
    then traverse matric and use those lists to check valid condition
    TODO: optimize space by using existing grid to mark valid nodes
    '''
    def countServers(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        row1s = [sum(grid[i]) for i in range(r)]
        col1s = [sum([grid[i][j] for i in range(r)]) for j in range(c)]
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (row1s[i] > 1 or col1s[j] > 1):
                    res += 1
        return res
