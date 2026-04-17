class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump = nums[0]

        def do(i, j):
            print(i, j)
            if i >= n - 1:
                return True

            jumps = range(1, j + 1)
            for jump in jumps:
                res = do(i + jump, nums[i + jump])
                if res:
                    return True

            return False

        return do(0, jump)