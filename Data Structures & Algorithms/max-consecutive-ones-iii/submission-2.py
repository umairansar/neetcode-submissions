class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max1s = 0
        l, r = 0, 0
        res = 0
        while r < n:
            if nums[r] == 1:
                max1s += 1
                r += 1
            elif k > 0:
                max1s += 1
                k -= 1
                r += 1
            elif k == 0 and nums[l] == 0:
                max1s -= 1
                k += 1
                l += 1
            elif k == 0 and nums[l] == 1:
                max1s -= 1
                l += 1
            res = max(res, max1s)
        return res