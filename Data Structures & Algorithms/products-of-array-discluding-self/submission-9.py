class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                val = nums[i - 1] * prefix[i - 1]
                prefix.append(val)
        
        suffix = []
        rums = nums[::-1]
        for i in range(len(rums)):
            if i == 0:
                suffix.append(1)
            else:
                val = rums[i - 1] * suffix[i - 1]
                suffix.append(val)

        suffix = suffix[::-1]
        print(prefix, suffix)

        res = [prefix[i] * suffix[i] for i in range(len(nums))]
        return res

        