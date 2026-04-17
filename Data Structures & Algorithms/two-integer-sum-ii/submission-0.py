class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = target - numbers[i]
            if j in numbers:
                return [i + 1, numbers.index(j) + 1]

        