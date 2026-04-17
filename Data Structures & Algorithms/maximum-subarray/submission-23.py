class Solution: #Top down O(n) time, O(n) space
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def calculate(i):
            if i in memo:
                return memo[i]
            if i == n-1:
                memo[i] = nums[i]
                return memo[i]
            memo[i] = nums[i] + max(0, calculate(i+1))
            return memo[i]

        calculate(0)
        return max(memo.values())

        #Bullshit mix of bottom up with top down
        # res = None
        # for i in range(n-1, -1, -1):
        #     res = calculate(i) if res is None else max(res, calculate(i))

        # return res