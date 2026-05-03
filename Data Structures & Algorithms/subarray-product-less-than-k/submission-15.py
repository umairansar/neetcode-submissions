class Solution: #O(n) time, O(1) space
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Improved sliding window w/o using explicit O(n) space for prefixes
        '''
        n = len(nums)
        curr = 1
        res = 0
        l, r = 0, 0
        while r < n:
            curr *= nums[r]
            while curr >= k and l <= r:
                curr //= nums[l]
                l += 1 
            res += r - l + 1
            r += 1
        return res
        