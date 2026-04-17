class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climbHelper(n_):
            if n_ <= 1:
                return 1
            
            cached = memo.get(n_)
            if cached:
                return cached

            memo[n_] = climbHelper(n_ - 1) + climbHelper(n_ - 2)
            return memo[n_] 
        
        return climbHelper(n)