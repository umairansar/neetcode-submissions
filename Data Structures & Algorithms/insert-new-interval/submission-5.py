class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and not newInterval:
            return []

        if not intervals and newInterval:
            return [newInterval]

        n = len(intervals)
        newIntervals = []
        newIntervalAdded = False
        for i in range(n):
            if not newIntervalAdded and newInterval[0] <= intervals[i][0]:
                newIntervals.append(newInterval)
                newIntervalAdded = True
            newIntervals.append(intervals[i])

        if not newIntervalAdded:
            newIntervals.append(newInterval)

        print("newIntervals", newIntervals)
        merged = [newIntervals[0]]
        for i in range(1, n+1):
            if newIntervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], newIntervals[i][1])
            else:
                merged.append(newIntervals[i])

        return merged