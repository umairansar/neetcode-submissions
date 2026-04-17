class Solution:
    def countSubstrings(self, s: str) -> int:

        memo = {}
        def check(l, r):
            if l < r:
                cached = memo.get((l, r))
                if cached:
                    return cached
                memo[(l, r)] = s[l] == s[r] and check(l+1, r-1)
                return memo[(l, r)]
            return True

        results = []
        n = len(s)
        for window in range(1, n+1):
            i = 0
            j = i + window - 1
            while j < n:
                if check(i, j):
                    results.append(s[i:i+window])
                i += 1
                j += 1
        
        return len(results)