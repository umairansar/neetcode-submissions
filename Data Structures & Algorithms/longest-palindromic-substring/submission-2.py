class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        def check(ss):
            l, r = 0, len(ss) - 1
            while l < r:
                if ss[l] != ss[r]:
                    return False
                l += 1
                r -= 1
            return True

        def brute(window):
            i = 0
            ret = ''
            while i + window != n + 1:
                if check(s[i:i+window]):
                    ret = s[i:i+window]
                i += 1
            return ret
        
        n = len(s)
        results = []
        for i in range(1, n + 1):
            results.append(brute(i))

        print(results)
        return max(results, key = len)