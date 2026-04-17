class Solution:
    '''
    create a dict of s1 counts, d1
    run sliding window on s2, if letter not in d1, move left to right
    if letter in d1, continue with moving right to end
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        targetCtr = {}
        for c in s1:
            targetCtr[c] = 1 + targetCtr.get(c, 0)

        windowCtr = {}
        l, r = 0, 0
        n = len(s2)
        while r < n:
            c = s2[r]
            print(c)
            if c not in targetCtr:
                l = r + 1
                windowCtr = {}
            else:
                windowCtr[c] = 1 + windowCtr.get(c, 0)
                print(".", windowCtr)
                while windowCtr[c] > targetCtr[c]:
                    windowCtr[s2[l]] -= 1 
                    l += 1
                if all(k in windowCtr and targetCtr[k] == windowCtr[k] for k in targetCtr) and (sum(targetCtr.values()) == sum(windowCtr.values())):
                    print("windowCtr", windowCtr, "targetCtr", targetCtr)
                    return True
            print(windowCtr)
            r += 1

        return False