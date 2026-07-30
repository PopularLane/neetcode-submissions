class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeroes = s.count("0")

        out = ""
        if ones <= 1:
            for x in range(zeroes):
                out += '0'
            out += '1'
        else:
            for x in range (ones - 1):
                out += '1'
            for x in range(zeroes):
                out += '0'
            out += '1'
        return out