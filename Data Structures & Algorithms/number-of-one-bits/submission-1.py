class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for s in range(32):
            if (1 << s) & n:
                result += 1
        return result
        