class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = max(nums)
        series = sum(range(m + 1))
        total = sum(nums)
        if series - total == 0:
            if 0 in nums:
                return m+1
            return 0
        return series - total
