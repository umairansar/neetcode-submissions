class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        while l < r:
            if mid == l:
                return min(nums[l], nums[r])
            if nums[r] < nums[l] and nums[r] < nums[mid]:
                l = mid
                mid = (l + r) // 2
            else:
                r = mid
                mid = (l + r) // 2
        return nums[mid]

        #rotated, right < left, so move right, and only move right if right < mid
        #move left