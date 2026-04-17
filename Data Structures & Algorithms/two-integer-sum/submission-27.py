class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_ = {}
        for i, v in enumerate(nums):
            if v in d_:
                return [d_[v], i]
            else:
                d_[target - v] = i