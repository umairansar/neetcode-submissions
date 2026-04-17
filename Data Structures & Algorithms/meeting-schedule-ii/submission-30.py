"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.end)
        print("append", intervals[0].start, intervals[0].end)
        rooms = [[intervals[0]]]

        for i in range(1, len(intervals)):
            closestRooms = [(j, intervals[i].start - room[-1].end) for j, room in enumerate(rooms)]
            closestRooms = list(filter(lambda x: x[1] >= 0 , closestRooms))
            if closestRooms:
                closestRoom, _ = min(closestRooms, key=lambda x: x[1])
                rooms[closestRoom].append(intervals[i])
            else:
                rooms.append([intervals[i]])
    
        print(list(map(lambda x: list(map(lambda y: (y.start, y.end), x)), rooms)))
        return len(rooms)