class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]
        count = 1

        n = len(intervals)
        for i in range(1, n):
            l, r = intervals[i]
            if l >= end:
                end = r
                count += 1
        
        return n - count
