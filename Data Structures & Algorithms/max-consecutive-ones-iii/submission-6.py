class Solution: # O(n) time, O(1) space
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max1s = 0 # no need to track min1s too
        l, r = 0, 0 # l, r init to 0
        res = 0
        while r < n: # r goes from 0 to n - 1
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