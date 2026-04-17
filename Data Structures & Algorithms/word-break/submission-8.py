class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def isInDict(w):
            for word in wordDict:
                if w == word:
                    return True
            return False

        memo = {}
        def check(i):
            if i in memo:
                return memo[i]
                
            if i == n:
                return True

            res = False
            for j in range(i+1, n+1):
                print(i, j, s[i: j])
                if isInDict(s[i:j]):
                    res = res or check(j)
            
            memo[i] = res
            return res

        n = len(s)
        return check(0)