class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            
            # if r < 0 or r >= rows or c < 0 or c >= cols:
            #     return

            visited.add((r, c))
            
            # down, right, up, left
            frontier = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
            for x, y in frontier:
                #out of bounds
                if x < 0 or x >= rows or y < 0 or y >= cols:
                    continue
                
                #already explored
                if (x, y) in visited:
                    continue
                
                #is water
                if grid[x][y] == "0":
                    continue

                #explore 
                dfs(x, y)
        
        visited: Set[Tuple[int, int]] = set()
        rows = len(grid)
        cols = len(grid[0])

        islands_count = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue
                
                if grid[row][col] == "0": 
                    continue

                dfs(row, col)
                print(visited)
                islands_count += 1
        
        return islands_count