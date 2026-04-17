class Solution:
    def minEatingSpeed(self, piles, h) -> int:
        n = len(piles)
        m = max(piles)
        
        l = 1
        r = m
        mid = r
        
        resH = m
        while l <= r:
            print(l, r, resH)
            mid = (l + r) // 2
            k = mid
            pilesCopy = piles[:]
            i, steps = 0, 0
            print("mid=", mid, " k=", k)
            # while i < n:
            #     pilesCopy[i] -= k
            #     if pilesCopy[i] <= 0:
            #         i += 1
            #     steps += 1
            steps = sum(math.ceil(pile/k) for pile in piles)
            print("steps=", steps)
            if steps <= h:
                r = mid - 1
                resH = min(resH, k)
            else:
                l = mid + 1
           
        return resH


