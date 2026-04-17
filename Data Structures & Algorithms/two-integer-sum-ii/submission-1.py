class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # O(n**2)
        # for i in range(len(numbers)):
        #     j = target - numbers[i]
        #     if j in numbers:
        #         return [i + 1, numbers.index(j) + 1]
        
        #O(n)
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
                continue
            
            if curSum < target:
                l += 1
                continue

            return [l + 1, r + 1]

            



        