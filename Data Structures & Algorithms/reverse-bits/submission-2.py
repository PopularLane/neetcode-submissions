class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for s in range(32):
            bit = (n >> s) & 1
            res += (bit << (31 - s))
        return res