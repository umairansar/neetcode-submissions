class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        step = 0
        print(n - 1)
        while r < n - 1:
            print(l, r)
            maxIdx = r
            updated = False
            for i in range(l, r + 1):
                if i + nums[i] > maxIdx:
                    maxIdx = i + nums[i]
                    updated = True
            if updated:
                step += 1
                l = r + 1
                r = maxIdx
        return step