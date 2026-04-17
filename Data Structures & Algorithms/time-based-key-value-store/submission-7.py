class TimeMap:

    def __init__(self):
        self.map = {}

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]

    # O(log n)
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.map:
            return res
        values = self.map[key]
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            val, t = values[mid]
            if t < timestamp:
                res = val
                l = mid + 1
            elif t > timestamp:
                r = mid - 1
            else:
                return val
        return res
        
