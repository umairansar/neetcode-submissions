class Solution: #O(n*m) time and space
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        def f(i, s): # form decision tree of depth O(2^n) if n levels w/o memo
            if i == n:
                return 1 if s == target else 0
            if (i, s) in memo:
                return memo[(i, s)]
            if target - s > suffix[i] or target - s < - suffix[i]: #pruning based on suffix
                return 0

            memo[(i, s)] = f(i + 1, s + nums[i]) + f(i + 1, s - nums[i])
            return memo[(i, s)]

        n = len(nums)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]
        return f(0, 0)