class Solution:
    '''
    Just thought of calculating diffs
    if some diffs are 0 store them as potential candidates for idx i
    don't store them if any other index positions in diff are -ve
    in the end check all positions have candidates in the end
    '''
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        diffs = [[x - y for x, y in zip(target, t)] for t in triplets]
        bucket = {i: False for i in range(len(target))}

        for tripletIdx, diff in enumerate(diffs): 
            if any(i < 0 for i in diff):
                continue 
                         
            for i in range(len(diff)):
                if diff[i] == 0:
                    bucket[i] = True

        return all(v for k, v in bucket.items())