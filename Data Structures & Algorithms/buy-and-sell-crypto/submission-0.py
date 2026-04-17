class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10, 1, 5, 6, 7, 1]
        # [0, -9, 4, 1 ,1, -6]
        # min [10, 1, 1, 1, 1, 1]
        # max [10, 7, 7, 7, 7, 1]
        l, r = 0, len(prices) - 1
        minimum, maximum = 100000, 0 
        mn = len(prices) * [minimum]
        mx = len(prices) * [maximum]
        while l <= r:
            minimum = min(minimum, prices[l])
            mn[l] = minimum
            l += 1
        
        l, r = 0, len(prices) - 1
        while l <= r:
            maximum = max(maximum, prices[r])
            mx[r] = maximum
            r -= 1
        res = []
        print(mn, mx)
        for k in range(len(prices)):
            res.append(mx[k] - mn[k])
        return max(res)