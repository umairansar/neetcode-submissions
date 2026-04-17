from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = reduce(lambda x, y: x * y, nums)
        if 0 in nums:
            nums_copy = nums[:]
            nums_copy.remove(0)
            total_without_zero = reduce(lambda x, y: x * y, nums_copy)
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(total_without_zero)
            else:
                res.append(total // nums[i])
        return res