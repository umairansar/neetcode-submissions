class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def isInDict(w):
            for word in wordDict:
                if w == word:
                    return True
            return False

        n = len(s)
        R = [False] * n
        R.append(True)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if isInDict(s[i: j]):
                    R[i] = (True and R[j]) or R[i] 

        print(R)
        return R[0]