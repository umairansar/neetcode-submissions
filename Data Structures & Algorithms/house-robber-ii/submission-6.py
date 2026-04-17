class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        n = len(nums)

        def helper(i, stop):
            if i == stop:
                return nums[i]

            if i == stop+1:
                return max(nums[i], nums[i-1])

            cached = memo.get((i, stop))
            if cached:
                return cached

            option1 = helper(i - 2, stop) + nums[i] if i - 2 >= stop else 0
            option2 = helper(i - 1, stop) if i - 1 >= stop else 0
            print("i", i, "stop", stop, " . ", option1, option2)
            memo[(i, stop)] = max(option1, option2)
            return memo[(i, stop)]

        print(helper(n - 2, 0))
        print(helper(n - 1, 1))
        return max(helper(n - 2, 0), helper(n - 1, 1))