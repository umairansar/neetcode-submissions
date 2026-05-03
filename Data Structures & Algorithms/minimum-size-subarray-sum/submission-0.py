class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        l, r = 0, 0
        res = float('inf')
        while r < n:
            if prefix[r+1] - prefix[l] < target:
                r += 1
            else:
                res = min(res, r-l+1)
                l += 1

        return 0 if res == float('inf') else res