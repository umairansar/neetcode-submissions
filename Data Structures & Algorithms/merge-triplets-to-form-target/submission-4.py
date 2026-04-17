class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        diffs = [[x - y for x, y in zip(target, t)] for t in triplets]
        bucket = {i: [] for i in range(len(target))}

        for tripletIdx, diff in enumerate(diffs):
            indices = []
            hasNeg = False
            for i in range(len(diff)):
                if diff[i] == 0:
                    indices.append(i)
                elif diff[i] < 0:
                    hasNeg = True

            if not hasNeg:
                for i in indices:
                    bucket[i] = tripletIdx
            
        return not any(v == [] for k, v in bucket.items())