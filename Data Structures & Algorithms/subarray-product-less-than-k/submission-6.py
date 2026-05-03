class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [1] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] * nums[i-1]
        prefix[0] = 1
        print(prefix)
        l, r = 0, 0
        map = {0:1}
        res = 0
        while r < n and l < n:
            print("l, r", l, r)
            if l > r:
                r = l
            if prefix[r+1] // prefix[l] < k:
                print("b",res)
                res += (r - l + 1)
                print("a",res)
                r += 1
            else:
                l += 1
        return res