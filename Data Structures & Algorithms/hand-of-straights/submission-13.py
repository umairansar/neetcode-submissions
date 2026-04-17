class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        heapq.heapify(hand)
        factor = len(hand) // groupSize
        print("factor", factor)
        res = [[] for _ in range(factor)]
        print("res", res)
        bucket = set(list(range(factor)))
        currs = defaultdict(set)
        while hand:
            print(currs, res)
            if not currs:
                curr = heapq.heappop(hand)
                res[0].append(curr)
                currs[curr+1].add(0)
                bucket.remove(0)
            else:
                next = hand[0]
                print(next)
                if next in currs:
                    if currs[next]:
                        f = currs[next].pop()
                    elif bucket:
                        f = bucket.pop()
                    else:
                        return False
                    print(f, res, len(res))
                    curr = heapq.heappop(hand)
                    res[f].append(curr)
                    if len(res[f]) < groupSize:
                        currs[curr+1].add(f)
                    bucket.discard(f)
                elif bucket:
                    f = bucket.pop()
                    curr = heapq.heappop(hand)
                    res[f].append(curr)
                    if len(res[f]) < groupSize:
                        currs[curr+1].add(f)
                    bucket.discard(f)
                else:
                    return False

        return True
        


