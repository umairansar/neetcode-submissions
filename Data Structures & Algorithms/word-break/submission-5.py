class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
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
                    remainingWord = word[r:]
                    memo[remainingWord] = check(remainingWord)
                    result = memo[remainingWord]
                    finalResult |= result 
                r += 1
            
            return finalResult   
        
        return check(s)