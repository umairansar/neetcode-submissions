class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1] # prefix includes current index value
        
        map = {0:0}
        for i in range(1, n+1):
            print(i, prefix[i], prefix[i] % k, prefix[i] % k in map)
            if prefix[i] % k in map and abs(map[prefix[i] % k] - i) > 1:
                return True
            if prefix[i] % k not in map:
                map[prefix[i] % k] = i
        return False