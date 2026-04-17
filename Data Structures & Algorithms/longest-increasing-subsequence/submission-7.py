class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def check(i):
            if i == n - 1:
                return 1
            
            res = 1
            j = i + 1
            while j < n:
                if nums[j] > nums[i]:
                    res = max(res, 1 + check(j)) #check(j) returns LIS where
                j += 1 # nums[j] is included in solution. Then I can be sure
            return res # that solution of i is 1 + solution of j granted j > i

        return max([check(i) for i in range(n)])