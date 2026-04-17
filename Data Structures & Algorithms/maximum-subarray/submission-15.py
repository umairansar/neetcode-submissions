class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        maxRes = nums[0]
        for i in range(1, n):
            if res < 0:
                res = nums[i]
            # elif res + nums[i] < 0: # new start
            #     res = 0
            else:
                res += nums[i]
            maxRes = max(maxRes, res)
        
        return maxRes
            
        # while i < n:
        #     if not res:
        #         res = nums[s]
        #     elif res + nums[i] < 0:
        #         s = i + 1
        #         res = None
        #     else:
        #         res += nums[i]
        #     i += 1 
        # return res
