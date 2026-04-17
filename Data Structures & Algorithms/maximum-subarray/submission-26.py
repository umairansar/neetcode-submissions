class Solution: # Best Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr = nums[0]
        res = nums[0]
        for i in range(1, n):
            if curr < 0:
                curr = 0
            curr += nums[i]
            res = max(res, curr)
        return res
            
        # n = len(nums)
        # res = nums[0]
        # maxRes = nums[0]
        # for i in range(1, n):
        #     if res < 0:
        #         res = nums[i]
        #     else:
        #         res += nums[i]
        #     maxRes = max(maxRes, res)
        
        # return maxRes

