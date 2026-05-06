class Solution:
    '''
    Trick is to proces events not time, since same time can be repeated for trips
    Fixes bug on leetcode (else block could be a while loop)
    trips = [[9,3,4],[9,1,7],[4,2,4],[7,4,5]]
    capacity = 23
    result = false
    expected = true
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        t = len(trips)
        starts = []
        ends = []
        for i in range(t):
            starts.append((trips[i][1], trips[i][0]))
            ends.append((trips[i][2], trips[i][0]))
        starts.sort()
        ends.sort()

        i, j = 0, 0
        res, cur = 0, 0
        while i < t and j < t:
            if starts[i][0] < ends[j][0]:
                cur += starts[i][1]
                i += 1
            elif starts[i][0] > ends[j][0]:
                cur -= ends[j][1]
                j += 1
            else:
                t_cur = starts[i][0]
                # Drain all starts and ends with the same time 
                while i < t and starts[i][0] == t_cur:
                    cur += starts[i][1]
                    i += 1
                while j < t and ends[j][0] == t_cur:
                    cur -= ends[j][1]
                    j += 1
            res = max(res, cur)
        return res <= capacity
