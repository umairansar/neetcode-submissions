class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Dict A: 4, B: 3, C:4
        AAABABB
        A: 1
        A: 2
        A: 3
        B: 1
        Find key with max val, A
        Dict[A] - Sum(x in Dict where x.key != A) <= k
        If yes: valid lcs till now
        If no: invalid, move left to right until valid (update dict)
        '''
        l, r = 0, 0
        lcs = 0
        counter = dict()
        while r < len(s):
            letter = s[r]
            counter[letter] = 1 + counter.get(letter, 0)
            r += 1
            max_letter = max(counter, key=counter.get)
            while sum(counter[k] for k in counter if k != max_letter) > k:
                counter[s[l]] -= 1
                l += 1
                max_letter = max(counter, key=counter.get)
    
            lcs = max(lcs, r - l)
        return lcs

        