class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if newInterval[0] < intervals[mid][0]:
                r = mid - 1 
            else:
                l = mid + 1
        
        intervals.insert(l, newInterval) 
        #always left used as insertion index

        n = len(intervals)
        merged = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged


