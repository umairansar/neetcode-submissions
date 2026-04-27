class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        memo = {}
        def dfs(i, j, k):
            if k == ls3:
                return i == ls1 and j == ls2
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            memo[(i, j, k)] = False
            if i != ls1 and s1[i] == s3[k]:
                memo[(i, j, k)] |= dfs(i+1, j, k+1)
            
            if memo[(i, j, k)]:
                return True
            
            if j != ls2 and s2[j] == s3[k] and j < ls2:
                memo[(i, j, k)] |= dfs(i, j+1, k+1)

            return memo[(i, j, k)]

        ls1 = len(s1)
        ls2 = len(s2)
        ls3 = len(s3)
        return dfs(0, 0, 0)
        