class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        memo = {}
        def dfs(i, total):
            if i == n or total > amount:
                return 0
            if total == amount:
                return 1
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = dfs(i, total + coins[i]) + dfs(i+1, total)
            return memo[(i, total)]
        
        return dfs(0, 0)