class Solution:
    def minEatingSpeed(self, piles, h) -> int:
        m = max(piles)
        l = 1
        r = m
        
        resH = m
        while l <= r:
            mid = (l + r) // 2
            k = mid
            # # pilesCopy = piles[:]
            # i, steps = 0, 0
            # while i < n:
            #     pilesCopy[i] -= k
            #     if pilesCopy[i] <= 0:
            #         i += 1
            #     steps += 1
            steps = sum(math.ceil(pile/k) for pile in piles)
            if steps <= h:
                r = mid - 1
                resH = min(resH, k)
            else:
                l = mid + 1
           
        return resH


