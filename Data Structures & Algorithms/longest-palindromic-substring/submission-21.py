class Solution:
    def longestPalindrome(self, s: str) -> str: # Memoization
        if len(s) == 1:
            return s

        memo = {}
        def check(i, j):
            if i < j:
                cached = memo.get((i, j))
                if cached:
                    return cached
                memo[(i, j)] = s[i] == s[j] and check(i+1, j-1) # top down
                return memo[(i, j)]
            return True

        def brute(window):
            i = 0
            ret = ''
            j = i + window - 1 #if window is 1, i and j should be same
            while j < n:
                if check(i, j):
                    ret = s[i:i + window] #but in s[:] j is one more cuz it is exclusive
                i += 1
                j += 1
            return ret
        
        n = len(s)
        results = []
        for window in range(1, n + 1):
            results.append(brute(window))

        return max(results, key=len)