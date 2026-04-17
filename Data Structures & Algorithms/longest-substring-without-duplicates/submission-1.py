class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = dict()
        l, r = 0, 0
        lcs = 0
        while r < len(s):
            letter = s[r]
            counter[letter] = 1 + counter.get(letter, 0)
            while counter[letter] > 1:
                print(counter, l, s[l])
                counter[s[l]] -= 1
                # letter = s[l]
                l += 1
            r += 1
            lcs = max(lcs, r - l)
        return lcs
