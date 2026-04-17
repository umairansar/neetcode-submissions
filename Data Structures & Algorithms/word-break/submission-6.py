class Solution: # Top Down with memoization
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: #O(n * m * t)
        
        def isInDict(w):
            for word in wordDict:
                if w == word:
                    return True
            return False

        memo = {}
        def check(word):
            n = len(word)
            if n == 0:
                return True
            
            if word in memo:
                return memo[word]
            
            finalResult = False
            l, r = 0, 1
            while r <= n:
                mySlice = word[l:r]
                if isInDict(mySlice):
                    result = check(word[r:])
                    finalResult |= result 
                r += 1
            
            memo[word] = finalResult
            return finalResult   
        
        return check(s)