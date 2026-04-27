class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        def dfs(i, j):
            if i == n:
                return m - j
            if j == m:
                return n - i
                
            if (i, j) in memo:
                return memo[(i, j)]

            if i < n and j < m and word1[i] == word2[j]:
                return dfs(i+1, j+1)

            replace = 1 + dfs(i+1, j+1)
            delete = 1 + dfs(i+1, j)
            insert = 1 + dfs(i, j+1) 
            memo[(i, j)] = min(replace, delete, insert)
            return memo[(i, j)]

        n = len(word1)
        m = len(word2)
        goal = max(n, m)
        return dfs(0, 0)