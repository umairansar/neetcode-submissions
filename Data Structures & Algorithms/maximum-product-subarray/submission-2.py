class Solution:
    def maxProduct(self, nums: List[int]) -> int: #2ptr
        n = len(nums)
        maxResults = []
        for i in range(n): # for each starting position
            r = i + 1
            res = nums[i]
            maxResult = res
            while r < n: # for each window until end 1*2, 1*2*-3, 1*2*-3*4
                res = res * nums[r]
                if res > maxResult:
                    maxResult = res
                r += 1
            maxResults.append(maxResult)
        return max(maxResults)

       