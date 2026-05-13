class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, reverse=True)
        times = [(target - p) / s for p, s in pairs]
        cur = 0
        res = 0
        for i in range(len(times)):
            if times[i] > cur:
                res += 1
                cur = times[i] # only update cur when new fleet detected
            # cur = times[i] # updating it every iter looses the current slowest leader of existing fleet e.g. failing case t=10 p=[4, 2, 0] s=[1, 3, 2] times=[6,2.833,5]
        return res