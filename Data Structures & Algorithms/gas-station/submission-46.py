class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        
        '''
        n = len(gas)
        overall = 0
        res = -1
        for i in range(n):
            oldOverall = overall
            overall += gas[i] - cost[i]
            delta = overall - oldOverall
            if delta >= 0 and res == -1:
                res = i
            if delta < 0 and overall < 0:
                res = -1
                    
        if overall < 0:
            res = -1

        return res