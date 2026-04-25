class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i == n or j == m:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i+1, j+1)
            else:
                memo[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            return memo[(i, j)]
        
        n = len(text1)
        m = len(text2)
        return dfs(0, 0)