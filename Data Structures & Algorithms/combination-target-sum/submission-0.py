class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(segment, summ):
            for n in nums:
                summ += n
                segment.append(n)
                if summ < target:
                    backtrack(segment, summ)
                elif summ == target:
                    freq = {}
                    for item in segment:
                        freq[item] = freq.get(item, 0) + 1
                    if freq not in resd:
                        resd.append(freq)
                        res.append(segment[:])
                summ -= n
                segment.pop()
                
        res = []
        resd = []
        backtrack([], 0)
        print(res)

        # resd = []
        # for r in res:
        #     freq = {}
        #     for item in r:
        #         freq[item] = freq.get(item, 0) + 1
        #     resd.append(freq)
        
        return res
        
