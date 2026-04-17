class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(segment, summ):
            for n in nums:
                summ += n
                segment.append(n)
                
                if summ < target:
                    dfs(segment, summ)
                elif summ == target:
                    #Create freq dict
                    freq = {}
                    for item in segment:
                        freq[item] = freq.get(item, 0) + 1
                    #Check if same dict not already in result
                    if freq not in resDict:
                        resDict.append(freq)
                        res.append(segment[:])
                
                #backtrack
                summ -= n
                segment.pop()
                
        res = []
        resDict = []
        dfs([], 0)
        return res
        
