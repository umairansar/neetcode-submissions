class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        n = len(nums)

        def dfs(i, count, summ):
            print(i, count, summ)
            if count >= n:
                return False

            if summ > target:
                return False

            if i == n-1:
                return summ == target 

            return dfs(i+1, count+1, summ+nums[i]) or dfs(i+1, count, summ)

        return dfs(0, 0, 0)