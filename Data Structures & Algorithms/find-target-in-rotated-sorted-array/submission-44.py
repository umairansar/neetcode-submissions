class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2
            if l == r - 1:
                if target == nums[l]:
                    return l
                elif target == nums[r]:
                    return r
                return -1

            # l, m sorted
            if nums[l] < nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid

            # m, r sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid
        
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        return -1
        