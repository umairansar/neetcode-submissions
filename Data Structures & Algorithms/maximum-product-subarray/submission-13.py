class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        results = []

        memo = {}
        def mul(l, r):
            if l > r:
                return 1

            if l == r or (r > n-1):
                return nums[l]

            if (l, r) in memo:
                return memo[(l, r)]

            memo[(l, r)] = nums[l] * mul(l+1, r)
            return memo[(l, r)]

        def count(w):
            i = 0
            j = i + w - 1
            res = -10000
            while j < n:
                print(i, i + w)
                res = max(res, mul(i, i + w))
                print(res)
                i += 1
                j += 1
            return res

        for window in range(1, n+1):
            results.append(count(window))

        print(results)
        return max(results)

