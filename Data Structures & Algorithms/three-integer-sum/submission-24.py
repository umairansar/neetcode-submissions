class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
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