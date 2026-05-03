class Solution: #O(n) time and space
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Not good idea to use prefix sum with sliding window
        Can do without extra space with simple sliding window
        '''
        n = len(nums)
        prefix = [1] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] * nums[i-1]
        l, r = 0, 0
        res = 0
        while r < n and l < n:
            if l > r:
                r = l
            if prefix[r+1] // prefix[l] < k:
                res += (r - l + 1)
                r += 1
            else:
                l += 1
        return res