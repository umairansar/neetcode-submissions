class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        print(0b1<<4)
        for i in range(32):
            count += 1 if (1 << i) & n != 0 else 0
        return count
        