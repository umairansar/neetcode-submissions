class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        at = n - 1
        goal = 0
        for i in range(n-2, -1, -1):
            if i + nums[i] >= at:
                at = i
        return at <= goal
            