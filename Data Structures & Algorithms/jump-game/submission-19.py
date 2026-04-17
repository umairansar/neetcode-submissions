class Solution:
    '''
    Greedy try but try next greedy option if 1st greedy does not work out
    '''
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump = nums[0]

        def do(i, j):
            print(i, j)
            if i >= n - 1:
                return True

            jumps = range(j, 0, -1)
            print(list(jumps))
            for jump in jumps:
                if i + jump >= n - 1:
                    return True
                res = do(i + jump, nums[i + jump])
                if res:
                    return True

            return False

        return do(0, jump)