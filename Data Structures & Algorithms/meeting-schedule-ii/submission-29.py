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

        # for i in range(1, len(intervals)):
        #     print(i, "print interval(", intervals[i].start,",", intervals[i].end,")")

        for i in range(1, len(intervals)):
            # print(i, "checking for interval",  intervals[i].start, intervals[i].end)
            closestRooms = [(j, intervals[i].start - room[-1].end) for j, room in enumerate(rooms)]
            # closestRooms = []
            # for i, room in enumerate(rooms):
            #     print(i, "interval(", intervals[i].start,",", intervals[i].end,")", room[-1].end)
            #     closestRooms.append((i, intervals[i].start - room[-1].end))
            print("r", intervals[i].start, rooms[-1][-1].end, closestRooms)
            closestRooms = list(filter(lambda x: x[1] >= 0 , closestRooms))
            print("r", intervals[i].start, rooms[-1][-1].end, closestRooms)
            if closestRooms:
                closestRoom, _ = min(closestRooms, key=lambda x: x[1])
                rooms[closestRoom].append(intervals[i])
            else:
                print("append", intervals[i].start, intervals[i].end)
                rooms.append([intervals[i]])
    
        print(list(map(lambda x: list(map(lambda y: (y.start, y.end), x)), rooms)))
        return len(rooms)