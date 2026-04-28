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

        # 