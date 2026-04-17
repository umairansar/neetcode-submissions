class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c: List[int] = [0] * (len(cost) + 1)
        
        if len(c) in [0, 1]:
            return 0
        
        for i in range(2, len(c)):
            c[i] = min(cost[i-1] + c[i-1], cost[i-2] + c[i-2])

        return c[-1]
        