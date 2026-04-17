from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = reduce(lambda x, y: x * y, nums)
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                nums_copy = nums[:]
                nums_copy.pop(i)
                res.append(reduce(lambda x, y: x * y, nums_copy))
            else:
                res.append(total // nums[i])
        return res