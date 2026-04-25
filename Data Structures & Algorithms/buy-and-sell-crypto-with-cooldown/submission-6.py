class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        memo = {}
        def dfs(i, bs):
            # print(i, bs)
            if i >= n:
                return 0
            if (i, bs) in memo:
                return memo[(i, bs)]

            if bs:
                memo[(i, bs)] = max(-prices[i] + dfs(i+1, not bs), dfs(i+1, bs))
            else:
                memo[(i, bs)] = max(prices[i] + dfs(i+2, not bs), dfs(i+1, bs))
            return memo[(i, bs)]

        n = len(prices)
        return max(0, dfs(0, True))