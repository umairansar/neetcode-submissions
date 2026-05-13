class Solution:
    #O(n) time and space
    def minRemoveToMakeValid(self, s: str) -> str:
        S = []
        delete = set() #[] optimization else last filter is O(n**2)
        for i in range(len(s)):
            if s[i] == "(": #or ord('a') <= s[i] ord('z'):
                S.append(i)
            elif s[i] == ")":
                if S:
                    S.pop()
                else:
                    delete.add(i)
        
        if S:
            delete.update(S)
        res = filter(lambda x: x[0] not in delete, enumerate(list(s)))
        return "".join(list(map(lambda x: x[1], res)))

