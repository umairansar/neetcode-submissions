class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n - 1, -1, -1):
            goal = nums[i]
            kp = k
            curr = 1
            for j in range(i - 1, -1, -1):
                if goal - nums[j] <= kp:
                    kp -= goal - nums[j]
                    curr += 1
            res = max(res, curr)
        return res