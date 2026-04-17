class Solution:
    def rob(self, nums: List[int]) -> int:
        reward: List[int] = [0] * len(nums)

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        reward[0] = nums[0]
        reward[1] = max(reward[0], nums[1])
        for i in range(2, len(reward)):
            reward[i] = max(reward[i - 2] + nums[i], reward[i-1])
        
        return max(reward)