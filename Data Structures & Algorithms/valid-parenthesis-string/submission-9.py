class Solution:
    def checkValidString(self, s: str) -> bool:
        CMin = 0
        CMax = 0
        for c in s:
            if c == "(":
                CMin += 1
                CMax += 1
            elif c == "*":
                CMin = max(0, CMin - 1) #consider )
                CMax += 1 #consider (
            else:
                CMin = max(0, CMin - 1)
                CMax -= 1
                if CMax < 0:
                    return False

        return CMin == 0 
