class Solution:
    def minEatingSpeed(self, piles, h) -> int: #O(n log m)
        m = max(piles)
        l = 1
        r = m
        
        resH = m
        while l <= r:
            k = (l + r) // 2
            # # pilesCopy = piles[:]
            # i, steps = 0, 0
            # while i < n:
            #     pilesCopy[i] -= k
            #     if pilesCopy[i] <= 0:
            #         i += 1
            #     steps += 1
            steps = sum(math.ceil(pile/k) for pile in piles)
            if steps <= h:
                r = k - 1
                resH = k
            else:
                l = k + 1
           
        return resH


