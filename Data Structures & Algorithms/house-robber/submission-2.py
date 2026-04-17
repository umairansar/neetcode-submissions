class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def helper(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            cached = memo.get(i)
            if cached:
                return cached
            memo[i] = max(helper(i - 1), nums[i] + helper(i - 2))
            return memo[i]

        return helper(n - 1)