class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        if n == 1:
            return 1
        l, r = 0, 1
        res = 0
        kp = k
        while r < n:
            goal = nums[r]
            oldGoal = nums[r-1]
            diff = goal - oldGoal
            if (r-l) * diff <= kp:
                res = max(res, r-l+1)
                kp -= (r-l) * diff
                r += 1
            else:
                kp += (oldGoal - nums[l])
                l += 1
        return res
            

