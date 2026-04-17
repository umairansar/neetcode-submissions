class Solution:
    def reverseBits(self, n: int) -> int:
        #return ~n & 0xFFFFFFFF
        x = 0
        for i in range(32):
            # bi = n & (1 << i) # this does not work because bit isolated but somewhere in middle
            bi = (n >> i) & 1
            x |= bi << (31 - i)
        return x