class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = nums[0]
        for n in nums[1:]:
            x = x ^ n
        return x