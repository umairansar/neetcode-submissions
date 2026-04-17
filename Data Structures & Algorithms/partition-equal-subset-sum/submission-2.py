class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        n = len(nums)

        def dfs(i, summ):
            if summ > target:
                return False

            if i == n-1:
                return summ == target 

            return dfs(i+1, summ+nums[i]) or dfs(i+1, summ)

        return dfs(0, 0)