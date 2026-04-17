class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            target = -1 * nums[i]
            difference = {}
            nums_right = nums[i+1:]
            for num in nums_right:
                if difference.get(num) != None:
                    res.add((nums[i], difference[num], num))
                else:
                    difference[target - num] = num
        
        res_unique = set()
        return list(map(list,res))