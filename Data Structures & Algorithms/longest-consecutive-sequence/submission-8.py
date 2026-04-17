class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0
        for num in nums:
            if num-1 in numSet:
                continue
            res = [num]
            next = num+1
            while next in numSet:
                res.append(next)
                next += 1
            if len(res) > result:
                result = len(res)
        return result