class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, i = 0, 1
        n = len(nums)
        res = nums[s]
        maxRes = nums[s]
        while i < n:
            if res < 0:
                s = i
                res = nums[i]
            elif res + nums[i] < 0: # new start
                s = i + 1
                res = 0
            else:
                res += nums[i]
            maxRes = max(maxRes, res)
            i += 1
        
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
