class Solution:
    def checkValidString(self, s: str) -> bool:
        C = []
        S = []
        for i, v in enumerate([*s]):
            # print(i)
            if v == "(":
                C.append(i)
            elif v == "*":
                S.append(i)
            else:
                if C:
                    C.pop()
                elif S:
                    S.pop()
                else:
                    return False
        
        print(C, S)
        for i in range(len(C)):            
            while True:
                if not S:
                    return False
                si = S.pop()
                if si > C[-1]:
                    break
            if si > C[-1]:
                C.pop()
        
        return not C




