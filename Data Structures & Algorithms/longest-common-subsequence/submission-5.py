class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        def dfs(i, j, sol):
            if i == n or j == m:
                return sol
            
            if (i, j, sol) in memo:
                return memo[(i, j, sol)]

            if text1[i] == text2[j]:
                memo[(i, j, sol)] = dfs(i+1, j+1, sol+1)
            else:
                memo[(i, j, sol)] = max(dfs(i+1, j, sol), dfs(i, j+1, sol))
            return memo[(i, j, sol)]
        
        n = len(text1)
        m = len(text2)
        return dfs(0, 0, 0)