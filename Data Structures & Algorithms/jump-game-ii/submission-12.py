class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        step = 0
        while r < n - 1:
            maxIdx = r
            for i in range(l, r + 1):
                if i + nums[i] > maxIdx:
                    maxIdx = i + nums[i]
            step += 1
            l = r + 1
            r = maxIdx
        return step