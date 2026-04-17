class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_sorted = nums
        nums_sorted.sort()
        # print(nums_sorted)

        for i, numi in enumerate(nums_sorted):
            
            if i > 0 and numi == nums_sorted[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            print(str(numi))

            while l < r:
                curSum = numi + nums_sorted[l] + nums_sorted[r]
                if curSum > 0:
                    r -= 1
                    continue

                if curSum < 0:
                    l += 1
                    continue

                res.append([numi, nums_sorted[l], nums_sorted[r]])
                # l = r +1
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
        
        return res
    
    def threeSumAttempt1(self, nums: List[int]) -> List[List[int]]:
        res = []
        d = dict()
        copy = set()

        for idx, num in enumerate(nums):
            d[num] = idx
        print(d)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                key = -(nums[i] + nums[j])
                if key in d:
                    print("key:" + str(key) + " i " + str(i) + " j " + str(j))
                    print(nums[i], nums[j], nums[d[key]])
                    print(copy)
                    if d[key] > j:
                        # i_in = i in copy
                        # j_in = j in copy
                        # k_in = d[key] in copy
                        if (nums[i], nums[j]) in copy: #(i_in and j_in) or (i_in and k_in) or (j_in and k_in):
                            continue
                        if (nums[j], nums[i]) in copy:
                            continue
                        if (nums[j], nums[d[key]]) in copy:
                            continue
                        if ( nums[d[key]], nums[j]) in copy:
                            continue
                        solution = [nums[i], nums[j], nums[d[key]]]
                        if solution in res:
                            continue
                        res.append(solution)
                        copy.update({(i, j)})
                # else:
                #     d[nums[j]] = j
        return res