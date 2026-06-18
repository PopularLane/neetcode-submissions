class Solution:
    def isArmstrong(self, n: int) -> bool:
        strN = str(n)
        digits = len(strN)
        res = 0

        for k in strN:
            res += int(k)**digits

        return res == n