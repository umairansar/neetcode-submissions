class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_unique = set(nums)
        if len(nums) > len(nums_unique):
            return True
        return False
        