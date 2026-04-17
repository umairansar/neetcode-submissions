class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        def helper(i, stop):
            if i == stop:
                return nums[i]

            if i == stop + 1:
                return max(nums[i], nums[i-1])

            cached = memo.get((i, stop))
            if cached:
                return cached

            memo[(i, stop)] = max(helper(i - 2, stop) + nums[i],  helper(i - 1, stop))
            return memo[(i, stop)]

        n = len(nums)
        return max(helper(n - 2, 0), helper(n - 1, 1))