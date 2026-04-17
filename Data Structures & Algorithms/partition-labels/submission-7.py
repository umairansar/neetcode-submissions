class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = {}
        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = [i, i]
            else:
                counter[s[i]][1] = i

        res = []
        partition = set()
        start = 0
        for i in range(len(s)):            
            partition.add(s[i])
            if i == counter[s[i]][1]:
                partition.remove(s[i])
            if not partition:
                res.append(i-start+1)
                start = i + 1
        
        return res

