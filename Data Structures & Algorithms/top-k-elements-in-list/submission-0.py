class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freaks = {}
        for num in nums:
            if num in freaks:
                freaks[num] += 1
            else: 
                freaks[num] = 1
        
        res = []
        for i in range(k):
            max_counter = -1
            max_value = -1
            for ke, va in freaks.items():
                if va > max_counter:
                    max_counter = va
                    max_value = ke
            freaks.pop(max_value)
            res.append(max_value)

        return res

        