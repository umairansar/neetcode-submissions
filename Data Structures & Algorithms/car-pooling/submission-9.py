class Solution: #O(n log n) time, O(n) space
    '''
    Sweep line pattern, simpler than solution 3 
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        t = len(trips)
        events = []
        for i in range(t):
            p, s, e = trips[i]
            events.append((s, p))
            events.append((e, -p))
        events.sort()
        cur = 0
        for event in events:
            cur += event[1]
            if cur > capacity:
                return False
        return True
