class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        n = len(nums)

        memo = {}
        def dfs(i, summ):
            if (i, summ) in memo:
                return memo[(i, summ)]
                
            if summ > target:
                return False

            if i == n-1:
                return summ == target 

            memo[(i, summ)] = dfs(i+1, summ+nums[i]) or dfs(i+1, summ)
            return memo[(i, summ)]

        return dfs(0, 0)