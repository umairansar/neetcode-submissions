class Solution:
    def maxProduct(self, nums: List[int]) -> int: #2ptr
        n = len(nums)
        maxResults = []
        for i in range(n):
            r = i + 1
            res = nums[i]
            maxResult = res
            while r < n:
                res = res * nums[r]
                if res > maxResult:
                    maxResult = res
                r += 1
            maxResults.append(maxResult)
        return max(maxResults)

       