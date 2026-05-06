class Solution:
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
                cur += starts[i][1]
                cur -= ends[j][1]
                i += 1
                j += 1
            res = max(res, cur)
        return res <= capacity
