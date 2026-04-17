class Solution: # Relies on 2 pointer O(n**2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = -1 * nums[i]
            nums_right = nums[i+1:]
            l = 0
            r = len(nums_right) - 1
            while l < r:
                l_num = nums_right[l]
                r_num = nums_right[r]
                if l_num + r_num < target:
                    l += 1
                elif l_num + r_num > target:
                    r -= 1
                else:
                    res.add((nums[i], l_num, r_num))
                    l += 1
        return list(map(list,res))
