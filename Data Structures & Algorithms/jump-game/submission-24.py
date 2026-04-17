class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        target = n - 1
        for k in range(n - 2, -1, -1):
            if k + nums[k] >= target:
                target = k
                if k == 0:
                    return True
        
        return False 