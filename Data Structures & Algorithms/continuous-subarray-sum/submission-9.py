class Solution:
    # O(n) time and spacee
    # Prefix Sum with Hashmap pattern
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1] # prefix includes current index value
        
        map = {0:0}
        for i in range(1, n+1):
            if prefix[i] % k in map:
                if abs(map[prefix[i] % k] - i) > 1:
                    return True
            else: 
                map[prefix[i] % k] = i # only add 1st occurence, handles 5, 0, 0, 0 case
        return False

        #nums:      [23,  2,  4,  6,  7], k = 6
        #prefix: [0, 23, 25, 29, 35, 42]
        #             j       i
        #             |       |
        #    in hashmap       in iter
        #hash map stores mod for each prefix
        #if some j prefix has same mod and later i had same mod
        #then their mods cancel to 0 i.e. their diff is multiple of k