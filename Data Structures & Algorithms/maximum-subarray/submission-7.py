class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        memo = {}
        '''
        calculate max subarray for n with solution starting at i
        '''
        def calculate(i):
            res = nums[i]
            maxRes = res
            for j in range(i+1, n):
                res += nums[j]
                if res > maxRes:
                    maxRes = res

            return maxRes

        res = None
        n = len(nums)
        for i in range(len(nums)-1, -1, -1):
            res = calculate(i) if res is None else max(res, calculate(i))

        return res

        