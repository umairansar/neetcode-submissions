class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = [target - i for i in nums]
        for j in range(len(nums)):
            nums_ = nums[:]
            nums_.pop(j)
            if diff[j] in nums_:
                return [j, 1 + nums_.index(diff[j])]