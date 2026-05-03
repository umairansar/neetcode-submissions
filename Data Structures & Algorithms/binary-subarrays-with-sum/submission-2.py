class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        map = {0:1}
        r = 0
        res = 0
        while r < n:
            # print(map)
            if prefix[r+1] - goal in map:
                res += map[prefix[r+1] - goal]
            map[prefix[r+1]] = 1 + map.get(prefix[r+1], 0)
            r += 1
        return res