class Solution: #O(n) time and space
    '''
    KEY: the window size determine new subsets added to result

    Not a good idea here to use prefix sums with sliding window
    We can reduce space to O(1) if we simply add elem to sum when r increments
    and reduce elem to sum when l increments.
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        l, r = 0, 0
        res = float('inf')
        while r < n: 
            #even though prefix is 0->n+1, sliding window goes from 0->n as prefix works from
            #r+1 to l to find range sum between l and r inclusive
            if prefix[r+1] - prefix[l] < target:
                r += 1
            else:
                res = min(res, r-l+1) # the window size determine new subsets added to result
                l += 1

        return 0 if res == float('inf') else res