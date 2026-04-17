class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: # with memoization
        n = len(nums)
        memo = {}
        def check(i):
            if i == n - 1:
                return 1
            
            res = 1
            j = i + 1
            while j < n:
                if nums[j] > nums[i]:
                    if j in memo:
                        res = max(res, memo[j])
                    else:
                        memo[j] = 1 + check(j) 
                        res = max(res, memo[j]) 
                j += 1 
            return res

        return max([check(i) for i in range(n)])