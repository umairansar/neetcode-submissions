class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: # with memoization
        n = len(nums)
        memo = {}
        def check(i):
            if i in memo:
                return memo[i]
            
            if i == n - 1:
                return 1

            res = 1
            j = i + 1
            while j < n:
                if nums[j] > nums[i]:
                    res = max(res, 1 + check(j)) 
                j += 1 
            
            memo[i] = res
            return res

        return max([check(i) for i in range(n)])