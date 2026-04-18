class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        dup = set()
        res = 0
        while r < n:
            if s[r] in dup:
                while l < r:
                    dup.remove(s[l])
                    if s[l] == s[r]:
                        l += 1
                        break
                    l += 1

            dup.add(s[r])
            res = max(r - l + 1, res)
            r += 1
        return res