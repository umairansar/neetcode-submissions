class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            #prefix[i] = prefix[i-1] + 0 if nums[i-1] else 1
            prefix[i] = prefix[i-1] + (0 if nums[i-1] else 1)

        res = 0
        for i in range(n):
            l, r = 0, i #fixing right boundary
            while l < r:
                m = (l + r) // 2
                if prefix[i+1] - prefix[m] <= k: # [m, i] is valid, can expand and m is part of solution
                    r = m
                else: # [m, i] is invalid, need to shrink and m is not part of solution 
                    l = m + 1
            res = max(res, i - l + 1) if prefix[i+1] - prefix[l] <= k else res
        return res
