class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        
        '''
        n = len(gas)
        s = 0
        c = 0
        g = gas[0]
        overall = 0

        diff = 0
        res = -1
        print("b)", c, g, overall)
        for i in range(n):
            c = cost[i]
            g = gas[i]
            oldOverall = overall
            overall -= c
            overall += g
            print("d", oldOverall, overall)
            delta = overall - oldOverall
            if delta >= 0 and res == -1: #g - c > diff:
                # diff = g - c
                print("set res", i)
                res = i
            if delta < 0 and overall < 0:
                res = -1
            
            print("a)", c, g, overall)
        
        if overall < 0:
            res = -1
        # c = g - cost[n - 1]
        # g = gas[0] + c
        # overall -= c
        # overall += g
        # if g - c > diff:
        #     diff = g - c
        #     res = n - 1
        # if overall < 0:
        #     res = -1
        # print("a)", c, g, overall)

        print(diff)

        return res