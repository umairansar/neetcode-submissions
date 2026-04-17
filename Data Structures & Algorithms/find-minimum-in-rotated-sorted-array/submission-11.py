class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        while l < r:
            n = nums[mid]
            if mid == l:
                return min(nums[l], nums[r])
            #rotated, right < left, so move right, and only move right if right < mid
            if nums[r] < nums[l] and nums[r] < nums[mid]:
                l = mid
                mid = (l + r) // 2
            else: #move left
                r = mid
                mid = (l + r) // 2
        return nums[mid]