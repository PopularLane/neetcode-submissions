class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for s in range(1, num + 1):
            square = s * s
            if square > num:
                return False
            if square == num:
                return True