class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def f(i, s):
            if i == n:
                return 1 if s == target else 0

            return f(i + 1, s + nums[i]) + f(i + 1, s - nums[i])

        n = len(nums)
        return f(0, 0)