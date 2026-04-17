class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, v in enumerate(nums):
            if (target-v) in mydict:
                return [mydict[target-v], i]
            mydict.update({v: i})
            
        # alt = []
        # numsSet = {}
        # for num in nums:
        #     alt.append(target - num)
        #     numsSet.update({num: target - num})
        
        # x = 0
        # for numi in alt:
        #     if (numi in numsSet):
        #         print(numi)
        #         print(alt)
        #         print(numsSet)
        #         idx1 = x
        #         idx2 = nums.index(numi)
        #         print("idx1", idx1)
        #         print("idx2", idx2)
        #         if (idx1 == idx2):
        #             numsCopy = nums[idx1+1:]
        #             print("numsCopy", numsCopy)
        #             if (numi in numsCopy):
        #                 idx2 = numsCopy.index(numi) + idx1 + 1
        #         if (idx1 != idx2):
        #             return [idx1, idx2]
        #     x += 1

        
        