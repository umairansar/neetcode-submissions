class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for s in strs:
            x = [0] * 26
            for letter in s:
                idx = ord(letter) - ord('a')
                x[idx] += 1
            key = tuple(x)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        print(groups)
        return list(groups.values())
        