class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        memo = {}
        def check(i, j):
            if i < j:
                cached = memo.get((i, j))
                if cached:
                    return cached
                memo[(i, j)] = s[i] == s[j] and check(i+1, j-1)
                return memo[(i, j)]
            return True

        def brute(window):
            i = 0
            ret = ''
            j = i + window - 1
            while j < n:
                if check(i, j):
                    ret = s[i:i + window]
                i += 1
                j += 1
            return ret
        
        n = len(s)
        results = []
        for window in range(1, n + 1):
            results.append(brute(window))

        return max(results, key=len)