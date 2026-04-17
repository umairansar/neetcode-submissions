class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def calculate(i):
            if i in memo:
                return memo[i]
            if i == n-1:
                return nums[i]
            memo[i] = nums[i] + max(0, calculate(i+1))
            return memo[i]

        res = None
        for i in range(n-1, -1, -1):
            res = calculate(i) if res is None else max(res, calculate(i))

        return res