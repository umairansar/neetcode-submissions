class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else: 
                freqs[num] = 1
        
        buckets = {}
        for key, val in freqs.items():
            if val in buckets:
                buckets[val].append(key)
            else:
                buckets[val] = [key]
        
        n = max(buckets.keys())
        print(freqs, buckets, n)
        res = []
        while len(res) != k:
            print(res)
            values = buckets.get(n)
            if values != None:
                res.extend(values)
            n -= 1
        
        return res
