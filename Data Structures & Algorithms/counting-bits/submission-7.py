class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101
        6 --> 110
        7 --> 111
        8 --> 1000
        '''

        res = [0] * (n + 1)
        print(res, len(res))
        offset = 1
        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i
            res[i] = 1 + res[i - offset]
            
        return res