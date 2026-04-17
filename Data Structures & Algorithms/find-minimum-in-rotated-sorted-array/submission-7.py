class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3, 4, 5, 6, 1, 2
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        while l < r:
            n = nums[mid]
            print("before", mid)
            if mid == l:
                return min(nums[l], nums[r])
            if nums[r] < nums[l] \
                and nums[r] < nums[mid]: #rotated, move right
                l = mid
                mid = (l + r) // 2
            else: #move left
                r = mid
                mid = (l + r) // 2
            print("after", mid)
        return nums[mid]