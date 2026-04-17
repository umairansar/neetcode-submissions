class Solution:
    def rob(self, nums: List[int]) -> int: #botton up
        if len(nums) == 1:
            return nums[0]
            
        gains = [0] * len(nums)
        gains[0] = nums[0]
        gains[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            gains[i] = max(gains[i - 2] + nums[i], gains[i - 1])
        
        return gains[-1]