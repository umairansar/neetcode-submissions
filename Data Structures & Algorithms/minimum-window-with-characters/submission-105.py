class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        OUZODYXAZV
        ^  ^^ ^    tracked indices via linked list T
        i
    
        vars: l, r, T, t_counter, window_counter, valids
        init l, r as 0
        start tracking from first occurence of elemetn in t
        then l, r = i, i
        if not valid:
            move r until valid found or end of s
        if valid:
            move l to next in T queue
        '''
        t_counter = {}
        for c in t:
            t_counter[c] = 1 + t_counter.get(c, 0)

        T = []
        for i in range(len(s)):
            if s[i] in t_counter:
                T.append(i)
        
        if not T:
            return ""

        valids = []
        seen = set()
        l, r = T[0], T[0]
        window_counter = {}
        while r < len(s):
            if s[r] in t_counter and r not in seen:
                window_counter[s[r]] = 1 + window_counter.get(s[r], 0)
            
            seen.add(r)
            
            # valid? save it and move l to next valid tracked position
            if all(t_counter[k] <= window_counter.get(k, 0) for k in t_counter):
                valids.append(s[l:r+1])
                if window_counter.get(s[T[0]]) != None:
                    window_counter[s[T[0]]] -= 1
                T = T[1:]
                if T:
                    l = T[0]
                else:
                    r += 1
           
            # invalid?
            else:
                r += 1

        print(valids)
        if len(valids) == 0:
            return "" 
        return min(valids, key=len) 
        
        