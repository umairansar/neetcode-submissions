class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            i = l
            while i < r:
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                i += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == k: return nums[p]
            if p > k: return quickSelect(l, p - 1)
            else: return quickSelect(p + 1, r)

        return quickSelect(0, len(nums) - 1)