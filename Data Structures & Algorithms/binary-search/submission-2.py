class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            print(l)
            print(mid)
            print (r)
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r = mid - 1
                continue
            
            if nums[mid] < target:
                l = mid + 1
                continue
        
        return -1
        