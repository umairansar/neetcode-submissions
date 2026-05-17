import math
class Solution:
    '''
    O(n) time and space
    '''
    def calculate(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        sList = []
        ops = set({"+", "-", "/", "*"})
        while r < n:
            if s[r] not in ops:
                r += 1
            else:
                sList.append(s[l:r])
                sList.append(s[r])
                r += 1
                l = r
        sList.append(s[l:])

        numStack = []
        opsStack = []
        i = 0
        n = len(sList)
        while i < n:
            token = sList[i]
            if token not in ops:
                numStack.append(token)
            else:
                opsStack.append(token)
                if token in ('/', '*'):
                    i += 1 
                    numStack.append(sList[i])
                    _ = opsStack.pop()
                    num2 = int(numStack.pop())
                    num1 = int(numStack.pop())
                    res = math.trunc(num1 / num2) if token == "/" else num1 * num2
                    numStack.append(res)
            i += 1

        res = int(numStack[0])
        for i in range(1, len(numStack)):
            op = opsStack.pop(0)
            res = res + int(numStack[i]) if op == "+" else res - int(numStack[i])
        return res