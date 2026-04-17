class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(segment, summ):
            for n in nums:
                summ += n
                segment.append(n)
                if summ < target:
                    backtrack(segment, summ)
                elif summ == target:
                    #Create freq dict
                    freq = {}
                    for item in segment:
                        freq[item] = freq.get(item, 0) + 1

                    #Check if same dict not already in result
                    if freq not in resDict:
                        resDict.append(freq)
                        res.append(segment[:])
                summ -= n
                segment.pop()
                
        res = []
        resDict = []
        backtrack([], 0)        
        return res
        
