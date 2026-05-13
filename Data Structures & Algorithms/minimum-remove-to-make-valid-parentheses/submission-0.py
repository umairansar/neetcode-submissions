class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        S = []
        delete = []
        for i in range(len(s)):
            if s[i] == "(": #or ord('a') <= s[i] ord('z'):
                S.append(i)
            elif s[i] == ")":
                if S:
                    S.pop()
                else:
                    delete.append(i)
        
        if S:
            delete.extend(S)
        res = filter(lambda x: x[0] not in delete, enumerate(list(s)))
        return "".join(list(map(lambda x: x[1], res)))

