class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def f(i, s): # form decision tree of depth O(2^n) if n levels
            if i == n:
                return 1 if s == target else 0
            if (i, s) in memo:
                return memo[(i, s)]

            memo[(i, s)] = f(i + 1, s + nums[i]) + f(i + 1, s - nums[i])
            return memo[(i, s)]

        n = len(nums)
        return f(0, 0)