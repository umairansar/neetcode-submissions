class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # track max_freq at insertion time in dict
        # istead of summing remaing every single time in while loop
        l, r = 0, 0
        lcs = 0
        counter = dict()
        max_freq = 0
        while r < len(s):
            letter = s[r]
            counter[letter] = 1 + counter.get(letter, 0)
            max_freq = max(max_freq, counter[letter]) 
            r += 1
            while (r-l) - max_freq > k: 
                counter[s[l]] -= 1
                l += 1
    
            lcs = max(lcs, r - l)
        return lcs