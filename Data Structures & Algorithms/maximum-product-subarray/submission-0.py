class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxResults = []
        for i in range(n):
            r = i + 1
            res = nums[i]
            maxResult = res
            print("starting i", i, res, maxResult)
            while r < n:
                res = res * nums[r]
                print("starting i", i, "r", r, res)
                if res > maxResult:
                    maxResult = res
                r += 1
            maxResults.append(maxResult)
        print(maxResults)
        return max(maxResults)

       