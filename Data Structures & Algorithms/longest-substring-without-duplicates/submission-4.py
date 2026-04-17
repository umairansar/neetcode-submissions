class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = dict()
        l, r = 0, 0
        lcs = 0
        while r < len(s):
            letter = s[r]
            counter[letter] = 1 + counter.get(letter, 0)
            while counter[letter] > 1:
                counter[s[l]] -= 1
                l += 1
            r += 1
            lcs = max(lcs, r - l)
        return lcs
