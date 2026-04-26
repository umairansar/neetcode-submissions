class Solution:
    '''
    Minimax problem - DP
    O(n * n) space because i goes to n and m can reach n
    O(n * n * n) time because of for loop
    '''
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        def dfs(i, m, ab):
            if i >= n:
                return 0
            if (i, m, ab) in memo:
                return memo[(i, m, ab)]

            res = 0 if ab else float('inf')
            if ab:
                for x in range(1, 2*m + 1):
                    curr = sum(piles[i:i+x]) #can be optimized
                    res = max(res, curr + dfs(i+x, max(m, x), not ab))
            else:
                for x in range(1, 2*m + 1):
                    res = min(res, dfs(i+x, max(m, x), not ab))
            memo[(i, m, ab)] = res
            return res

        n = len(piles)
        res = dfs(0, 1, True)
        return res