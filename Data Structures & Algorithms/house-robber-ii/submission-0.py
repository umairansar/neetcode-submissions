class Solution:
    def rob(self, nums: List[int]) -> int:
        reward_rob_first: List[int] = [0] * len(nums)
        reward_rob_last: List[int] = [0] * len(nums)

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        reward_rob_first[0] = nums[0]
        reward_rob_first[1] = max(reward_rob_first[0], nums[1])
        reward_rob_last[0] = 0
        reward_rob_last[1] = max(reward_rob_last[0], nums[1])

        for i in range(2, len(nums)):
            reward_rob_first[i] = max(reward_rob_first[i - 2] + nums[i], reward_rob_first[i-1])
            reward_rob_last[i] = max(reward_rob_last[i - 2] + nums[i], reward_rob_last[i-1])
        
        reward_rob_first[-1] = reward_rob_first[-2]
        return max(reward_rob_first[-1], reward_rob_last[-1])