class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, nums[0]
        res = 1
        while r < n - 1:
            nextR = r
            for i in range(l, r + 1):
                nextR = max(nextR, i + nums[i])
            r = max(r, nextR)
            res += 1
        return res