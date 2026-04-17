class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        memo = {}
        '''
        calculate max subarray for n with solution starting at i
        '''
        def calculate(i):
            if i in memo:
                return memo[i]

            res = nums[i]
            memo[i] = res
            print("i, n", i, n)
            for j in range(i+1, n):
                res += nums[j]
                if res > memo[i]:
                    memo[i] = res

            return memo[i] 

        res = None
        n = len(nums)
        for i in range(len(nums)-1, -1, -1):
            res = calculate(i) if res is None else max(res, calculate(i))
            print("i, cal, res", i, calculate(i), res)


        return res

        